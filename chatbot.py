import streamlit as st
import google.generativeai as genai
API_KEY= "AIzaSyBfea3okDI8wDK6iYTjZZu72W2MC8htuSU"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])
st.title(" Chatbot - Your AI Assistant")
st.write("Welcome to my chatbot! Ask me anything ! How can i help you!!")
if "messages" not in st.session_state:
  st.session_state.messages=[]
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt := st.chat_input("Say something.."):
  st.session_state.messages.append({"role":"user","content":prompt})  
  with st.chat_message("user"):
    st.markdown(prompt)
  responce=st.session_state.chat.send_message(prompt)
  st.session_state.messages.append({"role":"assistant","content":responce.text})
  with st.chat_message("assistant"):
    st.markdown(responce.text)
