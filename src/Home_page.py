import streamlit as st


def run():
    st.set_page_config(
        page_title="Home page",
        page_icon="👋",
    )

    st.write("# Привет! 👋")

    st.sidebar.success("Выберете раздел приложения выше.")

    st.markdown(
        """
       Это наше SUPER MULTI ML APP которое умеет все в мире МЛъя!
       
        **👈 Выберете что хотите от нашего приложения в сайдбаре**
        
        ## Используемая модель
    
        Сointegrated/rut5-base-multitask 
        *https://huggingface.co/cointegrated/rut5-base-multitask*
    
        **Команда**:
         - [Ильин В.Б.](https://github.com/Viktor-125142) – Лидер проекта
         - [Кравцов А.В.](https://github.com/Baddogel) – Инженер по машинному обучению
         - [Ефимович Е.А.](https://github.com/johnneon) – Full Stack-разработчик
         - [Крючков В.В.](https://github.com/Tifles) – Документалист/технический писатель
         - [Чашников С.Ю.](https://github.com/SergeyChashnikov)– Инженер MLOps
         - [Салов А.С.](https://github.com/TonyStranger404) – Scrum-мастер
    """
    )


if __name__ == "__main__":
    run()
