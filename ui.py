import streamlit as st

if "my_text" not in st.session_state:
    st.session_state.my_text = []

def submit():
    st.session_state.my_text.append(st.session_state.widget)
    st.session_state.widget = ""

def clear():
    st.session_state.my_text = []

st.button("Clear history", on_click=clear)
st.text_input("", key='widget', on_change=submit, placeholder='Say something!!')

user_chats = st.session_state.my_text

chat_entity = ["User:", "Chatbot:"]

for i in range(len(user_chats) - 1, -1, -1):
    st.write(chat_entity[i % 2])
    st.info(user_chats[i])