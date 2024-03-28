from streamlit.testing.v1 import AppTest


def test_text_area():
    at = AppTest.from_file("pages/1_📝_Summaraizer.py")

    at.run(timeout=30)

    text = """Данное исследование обусловлено широким использованием всенаправленной камеры и структурированного
    света в качестве источников получения информации из окружающей среды. Например, картографирование или
    реконструкция помещения и навигация мобильных роботов – это потенциальные приложения. Использование
    всенаправленной камеры дает широкий угол обзора, что является преимуществом в сравнении со стандартными
    камерами. В силу высокого искажения изображений может вызвать затруднения извлечение одинаковых пикселей между
    ними в случае со стереозрением. Более того, условия окружающей среды способны выводить из строя алгоритмы
    стереозрения, например, условия освещенности. Решение может быть найдено путем интеграции структурированного
    света в систему. Основным преимуществом использования структурированного света для анализа данных является его
    простой механизм обнаружения и извлечения из исходного изображения. Таким образом, система компьютерного зрения,
    состоящая из всенаправленной камеры в сочетании со структурированным светом, вызывает большой интерес среди
    ученых благодаря широкому углу обзора и высокой эффективности измерений. Для получения достоверных измерений
    система компьютерного зрения нуждается в калибровке. Это обусловлено тем, что без известной связи между камерой и
    лазерной плоскостью невозможно провести измерения соответствующим образом. Данное утверждение можно обосновать,
    проанализировав несколько существующих исследований. В работе [1] авторы проводили эксперименты с определенными
    допущениями, а именно: камера и лазерная плоскость были установлены параллельно полу. Экспериментальные данные
    оказались не такими точными, как ожидалось. Следует отметить, что даже небольшие перекосы могут привести к
    неправильным измерениям, что особенно важно для всенаправленной системы зрения, характеризующейся широким углом
    обзора. В данной статье авторы рассматривают модель системы компьютерного зрения, включающую в свой состав
    всенаправленную камеру и источник структурированного света, а также калибровку системы и дальнейшую оценку
    качества калибровочных параметров посредством построения 2D- и 3D-карт помещения. Отличительной особенностью
    данных методов является то, что можно произвести калибровку Для получения достоверных измерений система
    компьютерного зрения нуждается в калибровке."""

    at.text_area[0].set_value(text).run()

    at.button[0].click().run(timeout=60)
    assert (
        at.markdown[1].value
        == """Например, картографирование или реконструкция помещения и навигация мобильных роботов – это потенциальные приложения. В данной статье авторы рассматривают модель системы компьютерного зрения, включающую в свой состав всенаправленную камеру и источник структурированного света, а также калибровку системы и дальнейшую оценку качества калибровочных параметров посредством построения 2D- и 3D-карт помещения. Отличительной особенностью данных методов является то, что можно произвести Калибровку системы для получения достоверных измерений. Это обусловлено тем, что без известной связи между камерой и лазерной плоскостью невозможно провести измерения соответствующим образом. Эти данные оказались не такими точными, как ожидалось, но может быть найдено решение для анализа данных"""
    )


def test_title():
    at = AppTest.from_file("pages/1_📝_Summaraizer.py")

    at.run(timeout=30)

    assert at.title[0].value == "Конспектер"


def test_button():
    at = AppTest.from_file("pages/1_📝_Summaraizer.py")

    at.run(timeout=30)

    assert at.button[0].label == "Запуск"
