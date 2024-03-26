import streamlit as st
from src.app import components, session, constants
from src.model import (loadmodel_trans_ru_en,
                       interpreter,
                       loadmodel_trans_en_ru)


st.set_page_config(
    page_title="Translator Page",
    page_icon="🌏",
)


# Представление для выбора направления перевода
option = st.select_slider(
    'Выберите направление перевода:',
    options=['Русский-Английский', 'Английский-Русский'])


session.init()


# Рисуем шапку + описание
components.header(
    constants.LANG_PACK_TRANSLITE.get("title"),
    constants.LANG_PACK_TRANSLITE.get("subtitle"),
    constants.LANG_PACK_TRANSLITE.get("description"),
)

if option == 'Русский-Английский':
    with st.spinner('Загрузка модели для перевода с русского на английский...'):
        tokenizer, model = loadmodel_trans_ru_en()
elif option == 'Английский-Русский':
    with st.spinner('Загрузка модели для перевода с английского на русский...'):
        tokenizer, model = loadmodel_trans_en_ru()


# components.info("В общем страница переводчика например")

state = session.get_state()


text_area_data = components.text_area(
    constants.LANG_PACK_TRANSLITE.get("text_area_label"),
    state.text_area_disabled,
    constants.STATE_KEY_TEXT_AREA,
)


file_data = components.file_uploader(
    constants.LANG_PACK.get("file_uploader_label"),
    state.file_uploader_disabled,
    constants.STATE_KEY_FILE_UPLOADER,
)

btn = components.button(constants.LANG_PACK_TRANSLITE.get("btn_start_label"))


text = text_area_data or file_data


if text and btn:
    with components.spinner(text=constants.LANG_PACK_TRANSLITE.get("loading_result_text")):
        res = interpreter(text, tokenizer, model)

    components.results(constants.LANG_PACK_TRANSLITE.get("result_text"), res)
elif not text and btn:
    components.info(constants.LANG_PACK_TRANSLITE.get("empty_input_text"))
st.sidebar.markdown(
    """
    Переводчик
    Создано в рамках Проектного практикума «Персональный помощник для студентов». 
    """
)

