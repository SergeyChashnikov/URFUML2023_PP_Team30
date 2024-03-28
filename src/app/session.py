"""
Модуль сессии (или кеширования)

Модуль содержит в себе логику "состояния" приложения.
"""

import streamlit as st
from . import constants


def init_state():
    """Инициализация сессии стримлит"""
    st.session_state.file_uploader_disabled = (
        constants.STATE_KEY_FILE_UPLOADER in st.session_state
        and bool(st.session_state.text_area)
    )
    st.session_state.text_area_disabled = (
        constants.STATE_KEY_TEXT_AREA in st.session_state
        and bool(st.session_state.file_uploader)
    )


def get_state():
    """Геттер состояния стримлит приложения"""
    return st.session_state


def init():
    """Инициализация состояния приложения"""
    init_state()

