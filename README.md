# URFUML2023_PP_Team30
Проектный практикум

## Конспектер
### Персональный помощник для студентов

#### Frontend

Фронтенд часть написана с помощью библеотеки streamlit. В качестве "стейт-менджера" используется `streamlit session state`. Структура проекта следующая:
1. Основной код запуска приложения и безнес логика находится в `main.py`
2. Части приложения в директории `app`
    - `components.py` - вью компоненты
    - `constants.py` - константы
    - `session.py` - работа с состоянием приложения

Что бы запустить приложение, нужно выполнить команду `streamlit run main.py`.