import streamlit as st
# import streamlit.components.v1 as components
# import streamlit_analytics
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import STL
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline, Conversation
import tensorflow_hub as hub
import tensorflow as tf
from openai import OpenAI
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import os
import torch

OPENAI_API_KEY = "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"


# Set up Streamlit
st.set_page_config(page_title="Roast Session🔥",
                   page_icon=':chart_with_upwards_trend:', layout='wide')

st.title("Expense Expose")

right_column, left_column = st.columns(2)

with right_column:
    st.markdown(
        '''
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
            <p>Use our AI to discover the humor in your financial choices...</p>
            <p style="font-size: 2em;">🎤</p>
            <button style="width: 150px;">Get Started</button>
        </div>
        ''',
        unsafe_allow_html=True
    )
        
    
with left_column:
    st.image("./data/images/icon.png")
    st.markdown("🌟")
    expense_alert_col, comment_col = st.columns(2)
    with expense_alert_col:
        st.write("Test")
    with comment_col:
        st.markdown('''
                    Did you really need 10 pairs of the same shirt? You don't look good in them anyways :/
                    ''')
        st.markdown("🌟")
st.divider()

def log_in():
    st.markdown("<h2 style='text-align: center;'>Hi! I’m an AI that is trained to evaluate your spending habits. To get started, I’ll need to see your transactions. Please select your bank and log in.</h2>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>I won’t steal your credit card information and sell it on the dark web...</h3>", unsafe_allow_html=True)

    left_banks_col, right_banks_col = st.columns(2)
    
    if st.button(f"Log in with Vanguard"):
        uploaded_file = st.file_uploader("Upload your data file", type=["xlsx"])
        if uploaded_file is not None:
            data = pd.read_excel(uploaded_file)
            st.dataframe(data)
            return data

    banks = ["Wells Fargo", "Chase", "TD Bank", "Bank of America", "Santander", "Citi"]
    
    for bank in banks:
        if banks.index(bank) < len(banks) // 2: 
            with left_banks_col:
                st.button(f"Log in with {bank}", key=f"left_{bank}")
        else:  
            with right_banks_col:
                st.button(f"Log in with {bank}", key=f"right_{bank}")

    left_banks_col.markdown(
        f"<style>.stButton>button {{ width: 100%; margin: 0 auto; }}</style>",
        unsafe_allow_html=True,
    )
    right_banks_col.markdown(
        f"<style>.stButton>button {{ width: 100%; margin: 0 auto; }}</style>",
        unsafe_allow_html=True,
    )   
    st.divider()

    
# Results
def results():
    text_results, graph_results = st.columns(2)
    
    data = pd.read_excel("./data/Book1.xlsx")

    top_spending_category = data['category'].value_counts().idxmax()

    spending_by_category = data.groupby('category')['amount'].sum().reset_index()

    spending_by_category_sorted = spending_by_category.sort_values(by='amount', ascending=False)

    left_column_title = "Exposed or Economic?"
    right_column_title = "Spending Analysis"

    left_column_subtitle = f"I spend too much on:\n"
    left_column_subtitle += spending_by_category_sorted.to_string(index=False)

    right_column_subtitle = f"I had an unhealthy Obsession with:\n{top_spending_category}\nYou can’t run from your problems, they literally caught up to you"

    with text_results:
        st.markdown(f"## {left_column_title}")
        st.markdown(left_column_subtitle)

    with graph_results:
        st.markdown(f"## {right_column_title}")
        st.markdown(right_column_subtitle)

        fig = px.bar(spending_by_category_sorted, x="category", y="amount", title="Total Spending by Category")
        fig.update_layout(xaxis_title="Category", yaxis_title="Total Amount")

        st.plotly_chart(fig, use_container_width=True)
        

def chatbot():  
    st.sidebar.subheader("Talk to our AI about your financial habits!")

    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

    if 'history' not in st.session_state:
        st.session_state.history = []

    user_input = st.sidebar.text_input("Ask me anything about how to manage your finances better:", key="user_input")

    if st.sidebar.button("Submit", key="submit"):
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = new_user_input_ids if len(st.session_state.history) == 0 else torch.cat([st.session_state.history, new_user_input_ids], dim=-1)

        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        
        st.session_state.history = chat_history_ids
        
        st.sidebar.text_area("AI Response:", value=response, height=100, key="response")

        st.sidebar.write('<style>div.row-widget.stRadio {height: unset !important;} </style>', unsafe_allow_html=True)

def main():
    log_in()
    results()
    chatbot()
        
if __name__ == '__main__':
    main()
