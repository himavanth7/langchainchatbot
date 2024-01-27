from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader

def main():
    load_dotenv()
    st.set_page_config(page_title="chatbot")
    st.header("ASK YOUR CHATBOT")
    
    pdf = PdfReader('demo1.pdf')
    
    text = ""
    for page in pdf.pages:
        text+=page.extract_text()
        
    st.write(text)
        
    
    
    
    print(os.getenv("OPENAI_API_KEY"))



if __name__ == '__main__':
    main()