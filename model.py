import streamlit as st
import time

# Тут будет встраиваться модель
@st.cache_resource
def loadmodel():
  time.sleep(3)
  return ''


# Тут будет распологаться процессинг
def process(criteria: str):
  with open("result.txt") as result:
    time.sleep(3)
    return result.read()
