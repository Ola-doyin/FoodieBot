import streamlit as st
import os
from components.style import *
from components.prompt import *
import subprocess
import time
import socket
import sys
sys.dont_write_bytecode = True


#model = "gemini-2.5-flash"

# === Refresh database cache ===
backend_path = os.path.join("components", "backend.py")
# Check if backend is already running (optional but smart)
import socket
def is_backend_running(host="127.0.0.1", port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

# Launch backend.py
if not is_backend_running():
    for file in ["user.json", "menu.json", "branches.json"]:
        path = os.path.join(os.path.join(os.path.dirname(__file__), 'foodie_database'), file)
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"Removed {file}")
            except PermissionError as e:
                print(f"PermissionError: Could not remove {file}. {e}")
    subprocess.Popen(["python", backend_path])
    time.sleep(5)  # Give FastAPI time to start


# === Page config ===
st.set_page_config(page_title="FoodieApp", page_icon="🍲", layout="wide")
st.markdown(custom_sidebar_css(), unsafe_allow_html=True)

# === Sidebar: User Settings ===
def language_changed():
    pass

with st.sidebar:
    st.header("🛠️ Settings")
    st.write("Adjust profile and language here...")
    st.write("")
    language = st.selectbox(" ", ["English", "Yoruba", "Hausa", "Igbo", "Pidgin"], index=0, key="language_choice", on_change=language_changed)
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
st.markdown(page_subheader_css("Let’s find you something delicious — from Naija Jollof to Dodo Gizzard"), unsafe_allow_html=True)
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
    welcome_msg = generate_content(
        prompt_parts=persona_prompt,
        language=st.session_state["language"]
    )
    st.session_state.messages.append({"role": "bot", "content": welcome_msg})
    st.session_state.persona_sent = True


# === Display all messages using chat bubbles ===
for message in st.session_state.messages:
    role = message.get("role")
    content = message.get("content")

    if role in ["user", "bot"] and isinstance(content, str):
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

        response_text = generate_content(
            prompt_parts=build_prompt(
                user_text=prompt.text,
                name=st.session_state.get("name_input", None),
                image_count=0,
                language=st.session_state.get("language_choice", "English"),
                chat_history=st.session_state.messages
            ),
            language=st.session_state.get("language_choice", "English")
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

    elif prompt.files:
        if "uploaded_images" not in st.session_state:
            st.session_state.uploaded_images = []

        # Just get the first image for now (Gemini typically supports one at a time)
        image_file = prompt.files[0]
        st.session_state.uploaded_images.append(image_file)

        st.session_state.messages.append({
            "role": "user",
            "content": f"📷 Image uploaded: {image_file.name}" + (f"\n{prompt.text}" if prompt.text else "")
        })

        # Send to Gemini if text exists with the image
        if prompt.text:
            response_text = generate_image_content(
                image=image_file,
                prompt_parts=build_prompt(
                    user_text=prompt.text,
                    name=st.session_state.get("name_input", None),
                    image_count=1,
                    language=st.session_state.get("language_choice", "English"),
                    chat_history=st.session_state.messages
                ),
                language=st.session_state.get("language_choice", "English")
            )

            st.session_state.messages.append({"role": "bot", "content": response_text})

    st.rerun()
