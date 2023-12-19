import streamlit as st
from io import StringIO

def header(title: str, subheader: str, text: str):
  st.title(title)
  st.subheader(subheader)
  st.markdown(text)


def results(label: str, text: str):
  st.text(label)
  st.write(text)


def file_uploader(label: str, disabled: bool, state_key: str) -> str:
  uploaded_file = st.file_uploader(label, type="txt", disabled=disabled, key=state_key)
  result = ""

  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    result = string_data

  return result


def text_area(label: str, disabled: bool, state_key: str) -> str:
  return st.text_area(label, disabled=disabled, key=state_key)

def spinner(text: str):
  return st.spinner(text=text)

def button(text: str) -> bool:
  return st.button(text)

def info(text: str):
  return st.info(text)