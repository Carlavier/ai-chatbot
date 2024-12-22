import streamlit as st
import time

if "my_text" not in st.session_state:
    st.session_state.my_text = []

def append_chat(str):
    st.session_state.my_text.append(str)

def submit():
    st.session_state.my_text.append(st.session_state.widget)
    append_chat("Them chat cua ai o day alo!!!")
    st.session_state.widget = ""

def clear():
    st.session_state.my_text = []

st.button("Clear history", on_click=clear)
st.text_input("", key='widget', on_change=submit, placeholder='Say something!!')

chat_history = st.session_state.my_text

chat_entity = ["User:", "Chatbot:"]

if len(chat_history) > 0:
    # st.write(chat_entity[(len(chat_history) - 1) % 2])
    display_chat = ""
    chatbot_chat = st.empty()

for i in range(len(chat_history) - 2, -1, -1):
    # st.write(chat_entity[i % 2])
    if i % 2 == 0:
        st.markdown(
            "<div style='text-align: right;'>" + chat_history[i] + "</div>",
            unsafe_allow_html=True
        )
    else: st.write(chat_history[i])

if len(chat_history) > 0:
    for char in chat_history[-1]:
        display_chat += char
        chatbot_chat.write(display_chat)
        time.sleep(0.02)
