import streamlit as st
from analista import *
produto = st.text_input(label='',placeholder='Insira o produto desejado')
if produto:
    user = st.chat_message("user")
    user.write(produto)
    bot = st.chat_message("ai")
    bot.write(resposta(acessar_links(pesquisar_produto(produto))))
