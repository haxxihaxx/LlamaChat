from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os

st.header('Ollama local chat')
tab1, tab2 = st.tabs(["Chat","Settings"])
aimdl = 'llama3.2'
model = OllamaLLM(model = aimdl)
with tab2 : 
    st.title("Settings")
    optionai = st.selectbox(
    label='Choose Your AI Model',
    options= ('llama3.2', 'Mistral'),key=1, placeholder='')
    if optionai == "Mistral" : 
        aimdl = 'mistral'
        st.write('Don`t Have the Model ?') 
        btn1 = st.button(label="Install (4.0GB)",on_click=os.system('ollama install mistral'))
    elif optionai == "llama3.2":
        aimdl = 'llama3.2'
        st.write('Don`t Have the Model ?') 
        btn2 = st.button(label= 'install(2.0GB)', on_click=os.system('ollama install llama3.2'))
    st.caption('The AI Model is set to Llama3.2 by default.')

with tab1 :
    st.markdown('')
   
    while True  :
        answer = st.chat_input(key=f"USER")
        result = model.invoke(input = str(answer))
        msghuman = st.chat_message(name='human',avatar="👨🏻")
        msghuman.write(answer)
        msg = st.chat_message(name="ai",avatar="🤖")
        msg.write(result)

 