import streamlit as st
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

st.title('GPT Translator')

languages = ["", "German", "English", "Spanish", "French", "Chinese","German (Bavarian accent)","German (Swiss accent)", "Arabic", "Russian", "Portuguese", "Japanese", "Italian", "Hindi", "Bengali", "Urdu", "Korean", "Turkish", "Dutch", "Polish", "Vietnamese", "Thai", "Persian", "Indonesian", "Greek", "Swedish", "Czech", "Romanian", "Hungarian", "Finnish", "Danish", "Norwegian", "Hebrew", "Malay", "Ukrainian", "Slovak", "Croatian", "Serbian", "Bulgarian", "Lithuanian", "Latvian", "Estonian", "Slovenian", "Macedonian", "Albanian", "Maltese", "Icelandic", "Farsi", "Swahili", "Kurdish", "Pashto", "Tagalog"]

openai_api_key = st.sidebar.text_input('OpenAI API Key:', type='password')

selected_lang = st.sidebar.selectbox(
    "Select language:",
    languages,
    key = "selected_lang_1",
    index = 0
)


def generate_translation(input_text):
    chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
    messages = [
        SystemMessage(content=f"You are a translation expert. Translate the given text into {selected_lang}. Do not change the meaning of the text. Only return the translated text."),
        HumanMessage(content=input_text)
    ]
    info_placeholder = st.empty()
    answ = ""
    for chunk in chat.stream(messages):
        answ += chunk.content
        info_placeholder.info(answ)



with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    
    if submitted and openai_api_key.startswith('sk-'):
        generate_translation(text)


with st.container():
    if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠️')

with st.container():
    if not selected_lang  or selected_lang == languages[0]:
        st.warning('Please select a language!', icon='⚠️')
    
            


