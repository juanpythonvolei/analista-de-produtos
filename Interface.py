import streamlit as st
from analista import *
produto = st.chat_message("user")
if produto:
    produto.write(produto)
    bot = st.chat_message("ai")
    bot.write(resposta(acessar_links(pesquisar_produto(produto))))