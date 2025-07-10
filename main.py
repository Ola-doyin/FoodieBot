import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from components.style import *
from components.prompt import *
from components.chat import *
import sys
sys.dont_write_bytecode = True

# === Load Gemini API key ===
load_dotenv("./env.txt")
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# === Page config ===
st.set_page_config(page_title="FoodieApp", page_icon="🍲", layout="wide")
st.markdown(custom_sidebar_css(), unsafe_allow_html=True)

# === Sidebar: User Settings ===
with st.sidebar:
    st.header("🛠️ Settings")
    st.write("Adjust profile and language here...")
    st.write("")
    language = st.selectbox(" ", ["English", "Yoruba", "Hausa", "Igbo", "Pidgin"], index=0, key="language_choice")
    st.session_state["language"] = language 
    name = st.text_input(" ", key="name_input", placeholder="Enter your name")   

# === Paths ===
current_dir = os.path.dirname(__file__)
bg_path = os.path.join(current_dir, "assets", "background.png")
lg_path = os.path.join(current_dir, "assets", "logo.png")

# === Custom CSS and Page Branding ===
st.markdown(get_background_css(bg_path), unsafe_allow_html=True)
st.markdown(get_logo_css(lg_path, top='25%', left='8%', width='400px'), unsafe_allow_html=True)
st.markdown(page_header_css("Hi, I'm Foodie!👋"), unsafe_allow_html=True)
st.markdown(page_subheader_css("Let’s find you something delicious — from Naija Jollof to Jambalaya."), unsafe_allow_html=True)
st.markdown(custom_chat_input_css(), unsafe_allow_html=True)
st.markdown(transparent_header(), unsafe_allow_html=True)

# === Session state for messages ===
if "messages" not in st.session_state:
    st.session_state.messages = []

# === Send persona prompt and get first bot response ===
if (
    st.session_state.get("name_input") and
    st.session_state.get("language") and
    "persona_sent" not in st.session_state
):
    persona_prompt = build_persona(
        name=st.session_state["name_input"],
        language=st.session_state["language"]
    )
    st.session_state["persona"] = persona_prompt
    response = model.generate_content(persona_prompt)
    welcome_msg = response.text.strip()
    st.session_state.messages.append({"role": "bot", "content": welcome_msg})
    st.session_state.persona_sent = True

# === Display all messages using chat bubbles ===
for message in st.session_state.messages:
    role = message.get("role")
    content = message.get("content")

    if role in ["user", "bot"] and isinstance(content, str):
        # cleaned_content = content.strip().replace("\n", "<br>")
        # st.markdown(chat_bubble(role, cleaned_content), unsafe_allow_html=True)        
        st.markdown(chat_bubble(role, content), unsafe_allow_html=True)
    elif role == "user_image":
        st.image(content)

# === Chat Input ===
prompt = st.chat_input(
    "Type here and/or attach a food image...",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
    key="chat_input_main"
)

# === Handle input ===
if prompt:
    # Handle text input
    if prompt.text:
        st.session_state.messages.append({"role": "user", "content": prompt.text})
        
        # Call your response generator (fix: keyword args must be in order)
        response_text = generate_content(
            model,
            build_prompt(user_text=prompt.text, name=st.session_state.get("name", None),
                uploaded_files=None,
                language=st.session_state.get("language", "English"),
                chat_history=st.session_state.messages
            ),
            uploaded_files=None, language=st.session_state.get("language", "English")
        )
        
        st.session_state.messages.append({"role": "bot", "content": response_text})

    # Handle file uploads
    elif prompt.files:
        if "uploaded_images" not in st.session_state:
            st.session_state.uploaded_images = []

        for uploaded_file in prompt.files:
            st.session_state.uploaded_images.append(uploaded_file)
            st.session_state.messages.append({
                "role": "user",
                "content": f"📷 Image uploaded: {uploaded_file.name}"
            })

    st.rerun()

