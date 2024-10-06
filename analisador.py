import google.generativeai as genai
import streamlit as st
def analisar(pergunta):
    
    genai.configure(api_key=st.secrets["ia"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(pergunta)
    return response.text
