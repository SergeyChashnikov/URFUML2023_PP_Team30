import streamlit as st
from app import session, components, constants
import model
import questfunc


st.set_page_config(
    page_title="Question Generator",
    page_icon="❔",
)
session.init()

# Рисуем шапку + описание
components.header(
    "Генератор вопросов",
    "Задаём вопросы по исходному тексту",
    constants.LANG_PACK.get("description"),
)

# Подгружаем и кешируем модельку
with components.spinner(constants.LANG_PACK.get("loading_model_text")):
    tokenizer, model_rut5 = model.loadmodel()

# Получаем состояние приложения
state = session.get_state()

# Рисуем основные компоненты приложения, используя состояние,
# то есть если мы ввели текст, то сетим в состояние ключ
# file_uploader_disabled: True, и далее поле загрузки файла
# которое следит за этим полем в состоянии - отключается,
# и так же в обратном порядке для text_area с ключем text_area_disabled
text_area_data = components.text_area(
    constants.LANG_PACK.get("text_area_label"),
    state.text_area_disabled,
    constants.STATE_KEY_TEXT_AREA,
)


file_data = components.file_uploader(
    constants.LANG_PACK.get("file_uploader_label"),
    state.file_uploader_disabled,
    constants.STATE_KEY_FILE_UPLOADER,
)


# Получаем критерии (пропсы) для нашей модели, в нашем случае это просто текст
criteria = text_area_data or file_data

# Когда мы добавили текст, рисуем слайдеры для выбора количества
# и размера вопросов и кнопку запуска
text_len = int()
if criteria is not None:
    with components.spinner(
        text=constants.LANG_PACK.get("loading_result_text")
    ):
        text_len, res = questfunc.splitting_the_text(criteria)
# Получаем от пользователя требуемое количество вопросов
        if (text_len < 1):
            text_len = 1

        if (text_len == 1):
            st.text("Количество вопросов: 1")
            numb_of_quest = 1
        else:
            max_value = text_len+1
            numb_of_quest = st.slider(
                "Количество вопросов:",
                value=1,
                min_value=1,
                max_value=max_value,
                step=1
            )
# Получаем от пользователя максимальную длину вопроса
        max_length = st.slider(
            "Максимальная длина вопроса:",
            value=32,
            min_value=1,
            max_value=64,
            step=1
        )
# Отображаем кнопку запуска
        btn = components.button(constants.LANG_PACK.get("btn_start_label"))

# Если все ок, то передаем в функцию процессинга, если нет, то пишем что не так
if bool(criteria) and btn:
    result_list = questfunc.generate_questions(
            tokenizer,
            model_rut5,
            criteria,
            res,
            numb_of_quest,
            max_length
        )
# Выводим результат
    components.results(
        constants.LANG_PACK.get("result_text"),
        result_list
    )
# Если текст не загружен сообщаем об ошибке
elif not bool(criteria) and btn:
    components.info(constants.LANG_PACK.get("empty_input_text"))

st.sidebar.markdown(
    """
    # Приложение "Конспектор"
    Создано в рамках Проектного практикума
    «Персональный помощник для студентов».

    **Цель проектной работы**:
    разработка приложения для написания кратких конспектов,
    перевода или генерации вопросов на основании вводимого текста.

    Функцией приложения является сокращение объёма исходного текста
    с сохранением основных мыслей, перевод исходного текста,
    или генерация вопросов на его основе.
"""
)
