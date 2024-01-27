from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS



def main():
    load_dotenv()
    st.set_page_config(page_title="chatbot")
    st.header("ASK YOUR CHATBOT")
    
    pdf = PdfReader('demo1.pdf')
    
    text = ""
    for page in pdf.pages:
        text+=page.extract_text()
        

    #split into chunks
    
    text_splitter = CharacterTextSplitter(
        separator = "/n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    chunks = text_splitter.split_text(text)
    
    #create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    
    user_question = st.text_input("Ask a question about VVIT here: ")
    
    



        
    
    



if __name__ == '__main__':
    main()