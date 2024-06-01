import streamlit as st
from openai import OpenAI
import os
openai_api_key = st.secrets["openai_api_key"]
# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

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
