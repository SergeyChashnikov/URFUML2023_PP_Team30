"""
Модуль содержащий "вью" компоненты.
Логика следующая:
  Функции которые тут распологаются не должны хранить какой либо бизнес логики,
  при их вызове должны отрисовываться визуальные элементы приложения (интерфейс).
"""

import streamlit as st
from io import StringIO


def header(title: str, subheader: str, text: str):
    """
    Компонента шапки приложения, рендерит заголовок, подзаголовок и текст

    Параметры:
    title (str): Текст который будет использоваться в заголовке
    subheader (str): Текст который будет использоваться в подзаголовоке
    text (str): Текст который будет использоваться в текст под подзаголовоком XD
    """
    st.title(title)
    st.subheader(subheader)
    st.markdown(text)


def results(label: str, text: str):
    """
    Компонента результатов

    Параметры:
    label (str): Текст который будет использоваться как заголовок для отображения результатов
    text (str): Текст результат
    """
    st.text(label)
    st.write(text)


def file_uploader(label: str, disabled: bool, state_key: str) -> str:
    """
    Компонента загрузчика файлов

    Параметры:
    label (str): Лейбл поля загрузки файлов (плейсхолдер)
    disabled (bool): Флаг отвечающий за "отключение" поля загрузки
    state_key (str): Строка ключ или "id" который будет использоваться как
      ключ в закешированом состоянии стримлит приложения
    """

    uploaded_file = st.file_uploader(
        label, type="txt", disabled=disabled, key=state_key
    )
    result = ""

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        result = string_data

    return result


def text_area(label: str, disabled: bool, state_key: str) -> str:
    """
    Компонента поля для ввода

    Параметры:
    label (str): Лейбл поля ввода (плейсхолдер)
    disabled (bool): Флаг отвечающий за "отключение" поля ввода
    state_key (str): Строка ключ или "id" который будет использоваться как
      ключ в закешированом состоянии стримлит приложения
    """

    return st.text_area(label, disabled=disabled, key=state_key)


def spinner(text: str):
    """
    Компонента отображения загрузки, спинера с текстом рядом

    Параметры:
    text (str): Текст который будет отображаться рядом со спинером
    """

    return st.spinner(text=text)


def button(text: str) -> bool:
    """
    Компонента кнопки

    Параметры:
    text (str): Текст кнопки
    """

    return st.button(text)


def info(text: str):
    """
    Компонента "инфромационной вставки", визуально выделяется фоном и границей

    Параметры:
    text (str): Текст вставки
    """

    return st.info(text)
