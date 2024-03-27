import streamlit as st

from src.app.components import (header, results, file_uploader,
                                text_area, spinner, button, info)

from src.app.constants import (LANG_PACK_TRANSLITE,
                               STATE_KEY_FILE_UPLOADER,
                               STATE_KEY_TEXT_AREA)

from src.app.session import (init,
                             get_state)

from src.model import (loadmodel_translation_ru_en,
                       interpreter,
                       loadmodel_translation_en_ru)


st.set_page_config(
    page_title="Translator Page",
    page_icon="🌏",
)


# Представление для выбора направления перевода
option = st.select_slider(
    'Выберите направление перевода:',
    options=['Русский-Английский', 'Английский-Русский'])


init()


# Рисуем шапку + описание
header(
    LANG_PACK_TRANSLITE.get("title"),
    LANG_PACK_TRANSLITE.get("subtitle"),
    LANG_PACK_TRANSLITE.get("description"),
)

if option == 'Русский-Английский':
    with st.spinner(
            'Загрузка модели для перевода с русского на английский...'
    ):
        tokenizer, model = loadmodel_translation_ru_en()
elif option == 'Английский-Русский':
    with st.spinner(
            'Загрузка модели для перевода с английского на русский...'
    ):
        tokenizer, model = loadmodel_translation_en_ru()


# components.info("В общем страница переводчика например")

state = get_state()


text_area_data = text_area(
    LANG_PACK_TRANSLITE.get("text_area_label"),
    state.text_area_disabled,
    STATE_KEY_TEXT_AREA,
)


file_data = file_uploader(
    LANG_PACK_TRANSLITE.get("file_uploader_label"),
    state.file_uploader_disabled,
    STATE_KEY_FILE_UPLOADER,
)

btn = button(LANG_PACK_TRANSLITE.get("btn_start_label"))


text = text_area_data or file_data


if text and btn:
    with spinner(text=LANG_PACK_TRANSLITE.get("loading_result_text")):
        res = interpreter(text, tokenizer, model)

    results(LANG_PACK_TRANSLITE.get("result_text"), res)
elif not text and btn:
    info(LANG_PACK_TRANSLITE.get("empty_input_text"))
st.sidebar.markdown(
    """
    Переводчик
    Создано в рамках Проектного практикума
    «Персональный помощник для студентов».
    """
)
