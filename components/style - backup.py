import os
import base64
import sys
sys.dont_write_bytecode = True

def get_background_css(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Keeps the background fixed when scrolling */
        z-index: -1;  /* ensure it's behind everything */
    }}
    </style>
    """
    return css

def get_logo_css(image_path, top='15%', left='5%', width='150px'):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    css = f"""
    <style>
    .logo-fixed {{
        position: fixed;
        top: {top};
        left: {left};
        width: {width};
        z-index: 9999;
    }}
    .logo-fixed img {{
        width: 100%;
        height: auto;
    }}
    </style>
    <div class="logo-fixed">
        <img src="data:image/png;base64,{encoded_string}" alt="Logo">
    </div>
    """
    return css


def page_header_css(title_text):
    css = f"""
    <style>
    .custom-page-title {{
        position: fixed;
        top: 5%;
        left: 35%;        
        width: 65%;
        font-size: 48px;
        color: #ffffff;
        font-weight: bold;
        z-index: 9999;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
    }}
    </style>
    <div class="custom-page-title">{title_text}</div>
    """
    return css


def page_subheader_css(title_text):
    css = f"""
    <style>
    .custom-subheader {{
        position: fixed;
        top: 12%;
        left: 35%;
        width: 65%;
        font-size: 20px;
        color: #ff9933; 
        font-weight: 500;
        z-index: 999;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.6);
    }}
    </style>
    <div class="custom-subheader">{title_text}</div>
    """
    return css


def custom_chat_input_css():
    return """
    <style>
    /* Position and style the chat input box */
    div[data-testid="stChatInput"].st-emotion-cache-1eeryuo {
        position: fixed !important;
        left: 47% !important;
        width: 40% !important;
        bottom: 25px !important;
        z-index: 10000;
        border-radius: 8px !important;
        background-color: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* Style the inner container of the chat input */
    .st-emotion-cache-1eeryuo > div {
        background-color: white !important;
        border-radius: 18px !important;
    }

    /* Make immediate parent containers of file upload button white */
    .st-emotion-cache-x1bvup, .st-emotion-cache-nbth8s {
        background-color: #fff !important;
    }
    /* Style and clean up the chat input textarea */
    .st-emotion-cache-1eeryuo textarea {
        background-color: #fff !important;
        color: black !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        width: 100% !important;
        padding: 12px !important;

        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        border-radius: 0 !important;
    }
    /* Clear background of the full bottom container */
    .st-emotion-cache-1y34ygi[data-testid="stBottomBlockContainer"],
    .st-emotion-cache-hzygls {
        background-color: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* Placeholder styling */
    [data-testid="stChatInput"] textarea::placeholder {
        color: grey !important;
        font-style: italic;
        font-weight: 600 !important;
        font-size: 18px !important;
        background-color: #fff !important;
    }

    /* Input text color */
    [data-testid="stChatInput"] textarea {
        color: black !important;
        font-size: 20px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
        font-weight: 600 !important;
    }

    /* Icon (send, upload, etc.) styling */
    [data-testid="stChatInput"] svg {
        fill: grey !important;
        stroke: grey !important;
    }
    /* Force the chat input's inner container to align items vertically */
    div[data-testid="stChatInput"].st-emotion-cache-1eeryuo {
        display: flex !important;
        align-items: center !important;
    }

    /* Force inner divs (upload + send) to align center vertically too */
    .st-emotion-cache-x1bvup,
    .st-emotion-cache-sey4o0 {
        display: flex !important;
        align-items: center !important;
        height: 100% !important;
    }

    /* Align the textarea vertically in center with padding reset */
    .st-emotion-cache-1eeryuo textarea {
        margin-top: 4px !important;
        margin-bottom: 4px !important;
        padding-top: 6px !important;
        padding-bottom: 6px !important;
    }

    </style>
    """

def chat_bubble(sender, message):
    if sender == "bot":
        container_class = "bot-chat-container"
        bubble_class = "bot-bubble" 
        with open(os.path.join("assets", "bot.png"), "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        icon_url = f"data:image/png;base64,{encoded_icon}"
    else:
        container_class = "user-chat-container"
        bubble_class = "user-bubble"
        with open(os.path.join("assets", "user.png"), "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        icon_url = f"data:image/png;base64,{encoded_icon}"

    return f"""
    <style>
    .chat-container {{
        display: flex;
        margin: 10px 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        align-items: flex-start;
    }}

    .bot-chat-container {{
        justify-content: flex-start;
        margin-left: 43%;
        margin-right: 12%;
    }}

    .user-chat-container {{
        justify-content: flex-end;
        margin-left: 50%;
        margin-right: 5%;
    }}

    .bot-bubble, .user-bubble {{
        max-width: 100%;
        padding: 12px 18px;
        border-radius: 18px;
        font-size: 20px;
        font-weight: 500;
        line-height: 1.5;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        word-wrap: break-word;
    }}

    .bot-bubble {{
        background-color: #e0e0e0;
        color: #000;
    }}

    .user-bubble {{
        background-color: #ff9933;
        color: #000;
    }}

    .avatar {{
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 5px;
    }}

    .chat-content {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .chat-left .chat-content {{
        flex-direction: row;
    }}

    .chat-right .chat-content {{
        flex-direction: row-reverse;
    }}
    </style>

    <div class="chat-container {container_class} {'chat-left' if sender == 'bot' else 'chat-right'}">
        <div class="chat-content">
            <img class="avatar" src="{icon_url}" alt="{sender} icon" />
            <div class="{bubble_class}">{message}</div>
        </div>
    </div>
    """

    return """
    <style>
    div.st-ae div[data-testid="stVerticalBlock"][data-testid="stVerticalBlock"] {
        background-color: white !important; /* Make the popover content white */
        border: 1px solid #ddd !important;
    }

    /* 2. Style the "🌐 Select Language" markdown within the popover button */
    button[data-testid="stPopoverButton"] div[data-testid="stMarkdownContainer"] p {
        color: #333 !important; /* Example: make text dark grey */
        font-weight: bold !important;
        font-size: 16px !important;
    }

    /* Style the popover button itself */
    button[data-testid="stPopoverButton"] {
        background-color: #f0f0f0 !important; /* A light grey background for the button */
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
        padding: 0px 12px !important;
        box-shadow: none !important; /* Remove default button shadow if any */
    }

    /* 3. Style the "Choose your language:" markdown label inside the popover content */
    /* This targets the markdown container for the radio group label */
    label[data-testid="stWidgetLabel"] div[data-testid="stMarkdownContainer"] p {
        color: #555 !important; /* Darker grey for the label */
        font-size: 14px !important;
        font-style: italic !important;
        margin-bottom: 10px !important; /* Space below the label */
    }

    /* 4. Style the "English", "Yoruba", etc. markdown labels for the radio buttons */
    /* This targets the markdown containers for each radio option */
    label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p {
        color: #333 !important; /* Dark text for radio options */
        font-size: 15px !important;
        margin: 0 !important; /* Remove default paragraph margin */
    }

    /* Optional: Style the radio button circles themselves (might be tricky) */
    label[data-baseweb="radio"] .st-bz { /* The inner circle when unchecked */
        border-color: #888 !important;
    }
    label[data-baseweb="radio"] .st-be { /* The inner circle when checked */
        background-color: #1E90FF !important; /* Example: Dodger Blue for checked */
        border-color: #1E90FF !important;
    }

    /* General button SVG color for the popover button's dropdown arrow */
    button[data-testid="stPopoverButton"] svg {
        fill: #333 !important; /* Dark grey arrow */
    }
    </style>
    """

def custom_sidebar_css():
    return """
    <style>
    /* Increase sidebar width */
    section.stSidebar[data-testid="stSidebar"] {
        background-color: white !important;
        color: #333 !important;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1) !important;
        width: 320px !important; /* increase width */
    }

    /* Sidebar content area */
    div[data-testid="stSidebarContent"] {
        background-color: white !important;
        color: #333 !important;
    }

    /* Sidebar header */
    div[data-testid="stSidebarHeader"] {
        background-color: white !important;
        border-bottom: 1px solid #eee !important;
    }

    /* Sidebar collapse icon color */
    span[data-testid="stIconMaterial"] {
        color: #FF9933 !important;
        fill: #FF9933 !important;
    }

    /* Collapse button styling */
    button[data-testid="stBaseButton-headerNoPadding"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        pointer-events: auto !important;
    }
    </style>
    """