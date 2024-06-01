import streamlit as st
from openai import OpenAI
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-formanas-HAa5ntPi5XvOa0B2QpwTT3BlbkFJz4fYVfwl8inxMenGKluJ"

# Initialize OpenAI client
client = OpenAI()



# Streamlit app
st.title("Image and Query Input for OpenAI")

# Input image URL
image_url = st.text_input("Enter the image URL:")

# Input query
query = st.text_input("Enter your query:")

# Process the input and get response from OpenAI
if st.button("Get Response"):
    if image_url and query:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": query},
                        {"type": "image_url", "image_url": {"url": image_url, "detail": "high"}},
                    ],
                }
            ],
            max_tokens=300,
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter both an image URL and a query.")

# Run the app with: streamlit run app.py
