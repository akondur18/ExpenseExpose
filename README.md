## Inspiration
We took inspiration from Spotify Wrapped, a summary of the music you listened to throughout the year. However, we used this idea to provide users with a summary of their credit card transactions, allowing them to gain insights into their spending habits and make more informed financial decisions. 

## What it does
We created Expense Exposé, a personalized budgeting system that seamlessly integrates with users' credit card data, categorizing expenses and presenting them through intuitive visualizations. By leveraging AI algorithms, we offer tailored suggestions on saving money within specific categories, such as dining out or entertainment, empowering users to make informed financial decisions. Also, Expense Exposé provides personalized coaching, identifies recurring spending patterns, and offers strategies to improve financial health. To add a touch of humor and motivation, our hack incorporates a playful "roasting" feature where AI-generated comments gently poke fun at users' spending habits, encouraging them to stay mindful of their finances. With Expense Exposé, managing finances becomes both insightful and entertaining, guiding users toward their saving goals with ease.

## How we built it
We built Expense Exposé by first creating a mockup of our website design using Figma. We then imported the design to Streamlit, which used Python to create the visualization. Next, we used the Vanguard API to randomize data points to create a list of transactions. Using Pandas, Plotly, and Excel, we processed and analyzed this data, generating interactive visualizations to showcase users' spending patterns across various categories. Based on these insights, we used Google Cloud’s chatbot to provide personalized roasts and financial suggestions. 

## Challenges we ran into
We initially wanted to use AWS Amplify to visualize our Figma design, however, that platform required specific parameters that did not fit with our design. After doing some research, we found Streamlit, which made it easier to visualize our website design using Python. Another challenge we came across was finding a chatbot that would be compatible with our website. We first tried to integrate VertexAI, however, which had various limitations and therefore could not be used. As we did more research to find a chatbot, we found that the majority of them required a paid subscription, which isn’t accessible to many students. We finally decided to implement a chatbot using OpenAI, which was easily accessible and worked well with our website platform. 

## Accomplishments that we're proud of
We're immensely proud of several accomplishments achieved through our project. From developing an intuitive platform that simplifies complex financial data to integrating AI for personalized savings suggestions, we learned so much throughout this experience. By successfully combining diverse skill sets and overcoming technical hurdles, we've not only created a valuable tool for financial management but also contributed to enhancing users' financial literacy and well-being. Our achievements reflect our commitment to innovation, collaboration, and making a positive impact in the realm of personal finance.



## What we learned
Through this experience, we learned the value of collaboration across different areas of expertise. By combining design skills with data analysis and software development, we created a platform that's both user-friendly and informative. Working together, we realized how visualization and storytelling can make financial information more accessible and engaging. We also learned that integrating external data sources taught us practical lessons in data handling. Overall, this project was a hands-on learning experience that highlighted the importance of teamwork, creativity, and adaptability in problem-solving.

## What's next for Expense Exposé
In the next phase for Expense Exposé, we want to further enhance user engagement and motivation by training our model to deliver personalized roasts and suggestions based on the transaction data. To do so, we would have to refine our chatbot and use AI to analyze spending habits more deeply and generate insightful, yet lighthearted, commentary on users' financial behaviors. Through these advancements, Expense Exposé aims to become not only a trusted financial companion but also a source of encouragement and inspiration for users striving towards their financial goals.

