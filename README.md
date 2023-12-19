# приложение "Конспектор"

Создано в рамках Проектного практикума «Персональный помощник для студентов».

**Цель проектной работы:** разработка приложения для написания кратких конспектов вводимого текста.

**Задачи проектной работы:**
    1.	Изучить существующие предобученные модели нейронных сетей, предназначенных для написания краткого конспекта вводимого текста;
    2.	Написать на языке Python скрипт, реализующий преобразование вводимого текста в краткий конспект, с использованием готовой библиотеки машинного обучения;
    3.	Создать Web-приложение с пользовательским интерфейсом на основе написанного скрипта на Python;
    4.	Выполнить проверку и тестирование приложения;
    5.	Подготовить документацию.

**Функцией приложения** является сокращение объёма исходного текста с сохранением основных мыслей.

## Начало работы

Что бы запустить приложение, нужно установить зависимости и запустить стримлит:
 - Установка зависимостей
```bash
pip install -r requirements.txt
```
 - запуск стримлит приложения
```bash
streamlit run src/main.py
```
## Использование

В появившемся окне браузера можно прикрепить файл с исходным тектом или сразу вставить исходный текст в тектовое поле. 
После нажатия кнопки "Запуск" будет сформировн краткий конспект исходного текста.

## Команда

**Ильин В.Б.** – лидер проекта (https://github.com/Viktor-125142).
**Кравцов А.В.** – инженер по машинному обучению (https://github.com/Baddogel).
**Ефимович Е.А.** – Full Stack-разработчик (https://github.com/johnneon).
**Крючков В.В.** – документалист/технический писатель (https://github.com/Tifles).
**Чашников С.Ю.**– Инженер MLOps (https://github.com/SergeyChashnikov). 
**Салов А.С.** – Scrum-мастер (https://github.com/TonyStranger404).

## Используемая модель

Сointegrated/rut5-base-multitask 
*https://huggingface.co/cointegrated/rut5-base-multitask*

#### Структура проекта

Фронтенд часть написана с помощью библиотеки streamlit. В качестве "стейт-менджера" используется `streamlit session state`. Структура проекта следующая:
1. Основной код запуска приложения и бизнес логика находится в `main.py`
2. Части приложения в директории `app`
    - `components.py` - вью компоненты
    - `constants.py` - константы
    - `session.py` - работа с состоянием приложения


