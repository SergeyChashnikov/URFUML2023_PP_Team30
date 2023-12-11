import streamlit as st
from app import constants

def init_state():
  st.session_state.file_uploader_disabled = constants.STATE_KEY_FILE_UPLOADER in st.session_state and bool(st.session_state.text_area)
  st.session_state.text_area_disabled = constants.STATE_KEY_TEXT_AREA in st.session_state and bool(st.session_state.file_uploader)

def get_state():
  return st.session_state

def init():
  st.set_page_config(
    page_title=constants.LANG_PACK.get("title"),
    page_icon="🧊",
    layout="centered",
  )

  init_state()