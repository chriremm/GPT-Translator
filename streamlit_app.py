import streamlit as st
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

st.title('GPT Translator')

languages = ["", "German", "English", "Spanish", "French", "Chinese","German with strong Bavarian accent","German with strong Swiss accent", "Arabic", "Russian", "Portuguese", "Japanese", "Italian", "Hindi", "Bengali", "Urdu", "Korean", "Turkish", "Dutch", "Polish", "Vietnamese", "Thai", "Persian", "Indonesian", "Greek", "Swedish", "Czech", "Romanian", "Hungarian", "Finnish", "Danish", "Norwegian", "Hebrew", "Malay", "Ukrainian", "Slovak", "Croatian", "Serbian", "Bulgarian", "Lithuanian", "Latvian", "Estonian", "Slovenian", "Macedonian", "Albanian", "Maltese", "Icelandic", "Farsi", "Swahili", "Kurdish", "Pashto", "Tagalog"]
styles = ["No change", "Simple", "Business", "Academic", "Technical", "Casual"]

openai_api_key = st.sidebar.text_input('OpenAI API Key:', type='password')

selected_lang = st.sidebar.selectbox(
    "Select language:",
    languages,
    key = "selected_lang",
    index = 0
)
selected_style = st.sidebar.selectbox(
    "Select style:",
    styles,
    key = "selected_style",
    index = 0
)

def select_style(style):
     if style == styles[0]:
          return ""
     elif style == styles[1]:
          return "Write clearly and directly, using straightforward language without complex sentence structures or specialized jargon. Aim to make the information as accessible and understandable as possible for a wide audience. Use everyday words and short sentences to avoid misunderstandings and enhance readability."
     elif style == styles[2]:
          return "Write formally and professionally, while being concise and to the point. Utilize industry-specific terminology appropriately, focusing on clear communication of business objectives, processes, and outcomes. Prefer active voice to passive constructions to emphasize action and responsibility."
     elif style == styles[3]:
          return "Write formally, using specific terminology common within a field of study. Structure your text around thorough arguments, critical analysis, and evidence from reliable sources. "
     elif style == styles[4]:
          return "Write with clarity and precision to describe complex technical information and processes. Incorporate technical jargon and detailed explanations necessary for understanding the topic at hand. "
     elif style == styles[5]:
          return "Write in a relaxed and personal tone, including informal expressions and slang where appropriate. Reflect the way people communicate in everyday conversations. This style is suitable for texts aimed at establishing a personal connection with the reader or addressing topics in a light and engaging manner."


def generate_translation(input_text):
    chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
    style = select_style(selected_style)
    messages = [
        SystemMessage(content=f"You are a translation expert. Translate the given text into {selected_lang}. Only return the translated text.{style} When the input is blank, just ask for an input in english."),
        HumanMessage(content=input_text)
    ]
    info_placeholder = st.empty()
    answ = ""
    for chunk in chat.stream(messages):
        answ += chunk.content
        info_placeholder.info(answ)
    # st.info(messages)



with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    
    if submitted and openai_api_key.startswith('sk-') and not selected_lang == "":
        generate_translation(text)


with st.container():
    if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠️')

with st.container():
    if not selected_lang  or selected_lang == languages[0]:
        st.warning('Please select a language!', icon='⚠️')
    
            


