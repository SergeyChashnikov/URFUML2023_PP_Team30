from streamlit.testing.v1 import AppTest


def test_translation():
    # Запускаем приложение
    at = AppTest.from_file("pages/2_🌏_Translator.py")
    at.run(timeout=30)

    text = 'Привет'

    # Вводим текст для перевода
    at.text_area[0].set_value(text).run()

    # Нажимаем кнопку для начала перевода
    at.button[0].click().run(timeout=60)

    # Проверяем, что результат перевода отображается на странице
    # Здесь нужно заменить "Expected translation" на ожидаемый результат перевода
    assert (
             at.markdown[1].value
             == """Hello"""
             )


