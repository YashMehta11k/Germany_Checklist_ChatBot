import streamlit as st
import os
import openai
from lyzr import QABot

# Set up your OpenAI API key (ensure to keep it secure in production)
openai.api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = openai.api_key

def process_pdf(file_path, query):
    """Process the provided PDF file and return the response for the query."""
    if file_path is not None and query is not None:
        # Initialize QABot
        qa_bot = QABot.pdf_qa(input_files=[file_path])
        response = qa_bot.query(query)
        return response.response

# Streamlit page configuration
st.set_page_config(page_title='PDF QA Bot', layout='wide')

# App title
st.title('Germany Arrival Checklist Query Bot')

# File path (assuming the PDF file is in the same directory as your script)
file_name = "Arrival in Germany Checklist.pdf"
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Query text input
query = st.text_input("Enter your query")

# Submit button
if st.button('Submit'):
    if os.path.isfile(file_path) and query != "":
        result = process_pdf(file_path, query)
        st.write(result)
    else:
        st.warning("Please ensure the file exists and enter a query.")
