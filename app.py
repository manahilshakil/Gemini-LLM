import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

#loading all env variables
load_dotenv() 

genai.configure(api_key =os.getenv('GOOGLE_API_KEY'))

#importing gen model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#streamlit frontend
st.set_page_config(page_title= 'Q/A ChatBot', page_icon='')

st.header('Gemini LLM')

input = st.text_input('Ask me a question my Lady:', key='input')

submit = st.button('Submit')

#on submit
if submit:
    response = get_gemini_response(input)
    st.subheader('Heres your response')
    st.write(response)