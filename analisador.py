import google.generativeai as genai
import streamlit as st
def analisar(pergunta,conteudo):
    
    genai.configure(api_key=st.secrets['ia'])
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[{"role": "user", "parts": [{"text": conteudo}]}])
    response = chat.send_message(pergunta)
    return response.text
