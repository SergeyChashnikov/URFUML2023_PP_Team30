import streamlit as st
from app import components, session


st.set_page_config(
    page_title="Translator Page",
    page_icon="🌏",
)
session.init()
# Рисуем шапку + описание
components.header(
    "Переводчик",
    "Переводим тексты и мексиканцев через границу бесплатно",
    "(шучу, тексты не переводим)",
)

components.info("В общем страница переводчика например")

st.sidebar.markdown(
    """
    Переводчик
    Создано в рамках Проектного практикума
    «Персональный помощник для студентов».
    """
)
