import streamlit as st


# def page():
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.markdown("# 👈 тебе сюда ")
st.header("An owl")
st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.sidebar.markdown(
    """
    potato 
    """
)
