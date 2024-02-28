import streamlit as st
from lyzr import QABot

# Streamlit app
st.title("Question Answering with OpenAI")

# Initialize QABot
qa_bot = QABot.pdf_qa(input_files=["/content/Arrival in Germany Checklist.pdf"])

# User input for question
question = st.text_input("Ask a question about the document:")

if st.button("Get Answer"):
    # Get the API key from Streamlit secrets
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    
    # Set OpenAI API key
    qa_bot.set_openai_key(openai_api_key)
    
    # Query QABot for answer
    response = qa_bot.query(question)
    
    # Display answer
    if response.success:
        st.success(response.response)
    else:
        st.error("Unable to find an answer to the question. Please try again with a different question.")
