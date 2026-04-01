import streamlit as st
import plotly.express as px
import pandas as pd
import json
from datetime import datetime

from core.chatbot import get_chatbot_response
from core.summarizer import summarize_text
from core.quiz_generator import generate_quiz
from core.answer_generator import generate_answer
from core.file_handler import extract_text_from_file
from core.keyword_extractor import extract_keywords
from core.image_generator import generate_image
from core.export_utils import export_history_as_txt

st.set_page_config(
    page_title="Student Learning Assistant",
    page_icon="\U0001F393",
    layout="wide",
    initial_sidebar_state="expanded"
)

DEFAULT_STATES = {
    "history": [],
    "pinned_prompts": [],
    "theme_mode": "Dark",
    "last_output": "",
    "last_keywords": [],
    "image_history": [],
    "current_page": "\U0001F3E0 Dashboard"
}

for key, value in DEFAULT_STATES.items():
    if key not in st.session_state:
        st.session_state[key] = value

PAGES = [
    "\U0001F3E0 Dashboard",
    "\U0001F4AC AI Chat Assistant",
    "\U0001F4DD Summarizer",
    "\u2753 Quiz Generator",
    "\U0001F4DA Answer Generator",
    "\U0001F511 Keyword Extractor",
    "\U0001F3A8 AI Image Generator",
    "\U0001F4DC History & Export"
]

def go_to(page_name):
    st.session_state.current_page = page_name

dark_mode = st.session_state.theme_mode == "Dark"

if dark_mode:
    bg_gradient = "linear-gradient(135deg, #0B1020 0%, #111827 45%, #0F172A 100%)"
    glass_bg = "rgba(255,255,255,0.08)"
    glass_bg_strong = "rgba(255,255,255,0.10)"
    card_color = "rgba(255,255,255,0.06)"
    text_color = "#F8FAFC"
    sub_text = "#CBD5E1"
    accent = "#38BDF8"
    accent_2 = "#8B5CF6"
    border_color = "rgba(255,255,255,0.14)"
    shadow = "0 10px 30px rgba(0,0,0,0.35)"
else:
    bg_gradient = "linear-gradient(135deg, #F8FAFC 0%, #E0F2FE 45%, #EEF2FF 100%)"
    glass_bg = "rgba(255,255,255,0.70)"
    glass_bg_strong = "rgba(255,255,255,0.82)"
    card_color = "rgba(255,255,255,0.78)"
    text_color = "#0F172A"
    sub_text = "#475569"
    accent = "#2563EB"
    accent_2 = "#7C3AED"
    border_color = "rgba(15,23,42,0.08)"
    shadow = "0 10px 24px rgba(15,23,42,0.10)"

st.markdown(f"""
<style>
    .stApp {{
        background: {bg_gradient};
        color: {text_color};
        animation: fadeInPage 0.8s ease-in-out;
    }}

    @keyframes fadeInPage {{
        from {{
            opacity: 0;
            transform: translateY(10px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes floatGlow {{
        0% {{
            transform: translateY(0px);
            box-shadow: {shadow};
        }}
        50% {{
            transform: translateY(-4px);
            box-shadow: 0 14px 34px rgba(56,189,248,0.18);
        }}
        100% {{
            transform: translateY(0px);
            box-shadow: {shadow};
        }}
    }}

    @keyframes heroPulse {{
        0% {{
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }}
        50% {{
            box-shadow: 0 16px 42px rgba(56,189,248,0.18);
        }}
        100% {{
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }}
    }}

    @keyframes shine {{
        0% {{
            left: -100%;
        }}
        100% {{
            left: 120%;
        }}
    }}

    @keyframes metricPop {{
        0% {{
            opacity: 0;
            transform: scale(0.96) translateY(8px);
        }}
        100% {{
            opacity: 1;
            transform: scale(1) translateY(0);
        }}
    }}

    .block-container {{
        padding-top: 1.6rem;
        padding-bottom: 1.5rem;
    }}

    .hero-wrap {{
        background: {glass_bg};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {border_color};
        border-radius: 24px;
        padding: 22px 24px;
        box-shadow: {shadow};
        margin-bottom: 18px;
        animation: heroPulse 4s ease-in-out infinite;
    }}

    .main-title {{
        font-size: 2.4rem;
        font-weight: 800;
        color: {accent};
        margin-bottom: 0.15rem;
        letter-spacing: -0.4px;
    }}

    .sub-title {{
        font-size: 1rem;
        color: {sub_text};
        margin-bottom: 0.1rem;
    }}

    .top-nav-title {{
        font-size: 1rem;
        font-weight: 700;
        color: {accent};
        margin-bottom: 0.5rem;
    }}

    .glass-panel {{
        background: {glass_bg};
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid {border_color};
        border-radius: 22px;
        padding: 16px;
        box-shadow: {shadow};
        margin-bottom: 16px;
        animation: fadeInPage 0.7s ease;
    }}

    .feature-card {{
        position: relative;
        overflow: hidden;
        background: {glass_bg_strong};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {border_color};
        border-radius: 22px;
        padding: 18px;
        height: 210px;
        min-height: 210px;
        max-height: 210px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: {shadow};
        transition: all 0.30s ease;
        margin-bottom: 10px;
        animation: metricPop 0.6s ease;
    }}

    .feature-card::before {{
        content: "";
        position: absolute;
        top: 0;
        left: -120%;
        width: 60%;
        height: 100%;
        background: linear-gradient(
            120deg,
            transparent,
            rgba(255,255,255,0.18),
            transparent
        );
        transform: skewX(-20deg);
    }}

    .feature-card:hover::before {{
        animation: shine 0.9s ease;
    }}

    .feature-card:hover {{
        transform: translateY(-8px) scale(1.02);
        border: 1px solid {accent};
        box-shadow: 0 18px 40px rgba(56,189,248,0.22);
    }}

    .card-icon {{
        font-size: 2rem;
        margin-bottom: 0.35rem;
        transition: transform 0.3s ease;
    }}

    .feature-card:hover .card-icon {{
        transform: scale(1.08) rotate(-2deg);
    }}

    .card-title {{
        font-size: 1.08rem;
        font-weight: 800;
        color: {text_color};
        margin-bottom: 0.35rem;
    }}

    .card-desc {{
        font-size: 0.92rem;
        color: {sub_text};
        line-height: 1.45;
        min-height: 52px;
    }}

    .card-footer {{
        font-size: 0.82rem;
        color: {accent};
        font-weight: 700;
        margin-top: 8px;
    }}

    .metric-card {{
        background: {glass_bg};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid {border_color};
        border-radius: 20px;
        padding: 16px;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: {shadow};
        animation: floatGlow 3.5s ease-in-out infinite;
    }}

    .metric-number {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {accent};
    }}

    .metric-label {{
        font-size: 0.9rem;
        color: {sub_text};
        margin-top: 4px;
    }}

    .history-box {{
        background: {glass_bg};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 12px;
        border-radius: 14px;
        margin-bottom: 10px;
        border-left: 4px solid {accent};
        border: 1px solid {border_color};
        transition: all 0.25s ease;
    }}

    .history-box:hover {{
        transform: translateX(4px);
        border-left: 4px solid {accent_2};
    }}

    .keyword-chip {{
        display: inline-block;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 999px;
        background: linear-gradient(135deg, {accent}, {accent_2});
        color: white;
        font-size: 0.85rem;
        font-weight: 700;
        animation: metricPop 0.4s ease;
    }}

    .pinned-chip {{
        display: inline-block;
        padding: 8px 12px;
        margin: 4px 0;
        border-radius: 12px;
        background: rgba(245, 158, 11, 0.92);
        color: black;
        font-size: 0.85rem;
        font-weight: 700;
        width: 100%;
    }}

    div.stButton > button {{
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        padding: 0.65rem 0.9rem;
        border: 1px solid {border_color};
        transition: all 0.22s ease-in-out;
    }}

    div.stButton > button:hover {{
        border: 1px solid {accent};
        box-shadow: 0 0 0 2px rgba(56,189,248,0.14);
        transform: translateY(-2px);
    }}

    div.stDownloadButton > button {{
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        padding: 0.65rem 0.9rem;
    }}

    section[data-testid="stSidebar"] {{
        border-right: 1px solid {border_color};
        background: rgba(255,255,255,0.02);
    }}

    div[role="radiogroup"] label {{
        font-weight: 600 !important;
    }}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("\U0001F39B\uFE0F Control Panel")

theme_choice = st.sidebar.radio(
    "Theme Mode",
    ["Dark", "Light"],
    index=0 if st.session_state.theme_mode == "Dark" else 1
)
st.session_state.theme_mode = theme_choice

selected_sidebar = st.sidebar.selectbox(
    "Choose Feature",
    PAGES,
    index=PAGES.index(st.session_state.current_page)
)
st.session_state.current_page = selected_sidebar

st.sidebar.markdown("---")
st.sidebar.subheader("\U0001F4CC Pinned Prompts")

new_pin = st.sidebar.text_input("Pin a useful prompt")
if st.sidebar.button("\U0001F4CC Add Pin"):
    if new_pin.strip():
        st.session_state.pinned_prompts.append(new_pin.strip())
        st.sidebar.success("Prompt pinned!")

if st.session_state.pinned_prompts:
    for i, pin in enumerate(st.session_state.pinned_prompts):
        col_pin, col_del = st.sidebar.columns([4, 1])
        with col_pin:
            st.markdown(f"<div class='pinned-chip'>{pin}</div>", unsafe_allow_html=True)
        with col_del:
            if st.button("\u274C", key=f"remove_pin_{i}"):
                st.session_state.pinned_prompts.pop(i)
                st.rerun()
else:
    st.sidebar.caption("No pinned prompts yet.")

st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader("\U0001F4C2 Upload TXT or PDF", type=["txt", "pdf"])
file_text = extract_text_from_file(uploaded_file) if uploaded_file else ""

st.sidebar.markdown("---")
if st.sidebar.button("\U0001F5D1\uFE0F Clear History"):
    st.session_state.history = []
    st.session_state.last_output = ""
    st.session_state.last_keywords = []
    st.session_state.image_history = []
    st.sidebar.success("History cleared!")
    st.rerun()

st.markdown(f"""
<div class="hero-wrap">
    <div class="main-title">\U0001F393 Student Learning Assistant</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='top-nav-title'>\u26A1 Quick Navigation</div>", unsafe_allow_html=True)
nav_cols = st.columns(8)

top_nav_map = [
    ("\U0001F3E0", "\U0001F3E0 Dashboard", "nav_dash"),
    ("\U0001F4AC", "\U0001F4AC AI Chat Assistant", "nav_chat"),
    ("\U0001F4DD", "\U0001F4DD Summarizer", "nav_sum"),
    ("\u2753", "\u2753 Quiz Generator", "nav_quiz"),
    ("\U0001F4DA", "\U0001F4DA Answer Generator", "nav_ans"),
    ("\U0001F511", "\U0001F511 Keyword Extractor", "nav_key"),
    ("\U0001F3A8", "\U0001F3A8 AI Image Generator", "nav_img"),
    ("\U0001F4DC", "\U0001F4DC History & Export", "nav_hist"),
]

for idx, (label, page, key) in enumerate(top_nav_map):
    with nav_cols[idx]:
        if st.button(label, key=key):
            go_to(page)
            st.rerun()

st.markdown("")

def render_dashboard_card(icon, title, desc, footer, button_text, target_page, key):
    st.markdown(f"""
        <div class="feature-card">
            <div>
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-desc">{desc}</div>
            </div>
            <div class="card-footer">{footer}</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button(button_text, key=key):
        go_to(target_page)
        st.rerun()

def add_history(feature, user_input, output):
    st.session_state.history.append({
        "timestamp": str(datetime.now()),
        "feature": feature,
        "input": user_input,
        "output": output
    })

menu = st.session_state.current_page

if menu == "\U0001F3E0 Dashboard":
    st.subheader("\U0001F3E0 Ultra Dashboard")

    total_actions = len(st.session_state.history)
    total_pins = len(st.session_state.pinned_prompts)
    total_images = len(st.session_state.image_history)
    total_keywords = len(st.session_state.last_keywords)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>{total_actions}</div>
            <div class='metric-label'>Total Actions</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>{total_pins}</div>
            <div class='metric-label'>Pinned Prompts</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>{total_images}</div>
            <div class='metric-label'>Generated Images</div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>{total_keywords}</div>
            <div class='metric-label'>Last Keywords</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### \U0001F680 Quick Access Tools")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_dashboard_card(
            "\U0001F4AC", "AI Chat Assistant",
            "Ask academic questions and get smart AI-powered responses instantly.",
            "AI-powered academic help", "Open Chat",
            "\U0001F4AC AI Chat Assistant", "card_chat"
        )
    with c2:
        render_dashboard_card(
            "\U0001F4DD", "Smart Summarizer",
            "Convert long study notes, articles, or PDFs into short summaries.",
            "Fast note compression", "Open Summarizer",
            "\U0001F4DD Summarizer", "card_sum"
        )
    with c3:
        render_dashboard_card(
            "\u2753", "Quiz Generator",
            "Create practice quizzes from topics or uploaded study material.",
            "Revision booster", "Open Quiz",
            "\u2753 Quiz Generator", "card_quiz"
        )
    with c4:
        render_dashboard_card(
            "\U0001F4DA", "Answer Generator",
            "Generate university-style answers using your question and notes.",
            "Assignment-ready answers", "Open Answers",
            "\U0001F4DA Answer Generator", "card_ans"
        )

    c5, c6, c7, c8 = st.columns(4)
    with c5:
        render_dashboard_card(
            "\U0001F511", "Keyword Extractor",
            "Extract the most important keywords from your notes for revision.",
            "Smart revision tags", "Open Keywords",
            "\U0001F511 Keyword Extractor", "card_key"
        )
    with c6:
        render_dashboard_card(
            "\U0001F3A8", "AI Image Generator",
            "Generate creative visuals for assignments, posters, and presentations.",
            "Creative project visuals", "Open Image Tool",
            "\U0001F3A8 AI Image Generator", "card_img"
        )
    with c7:
        render_dashboard_card(
            "\U0001F4DC", "History & Export",
            "View all previous outputs and export your work in JSON or TXT format.",
            "Track your workflow", "Open History",
            "\U0001F4DC History & Export", "card_hist"
        )
    with c8:
        st.markdown(f"""
            <div class="feature-card">
                <div>
                    <div class="card-icon">\U0001F4C2</div>
                    <div class="card-title">Uploaded File Preview</div>
                    <div class="card-desc">Preview extracted content from your uploaded TXT or PDF file instantly.</div>
                </div>
                <div class="card-footer">Live content preview below</div>
            </div>
        """, unsafe_allow_html=True)

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("### \U0001F4CA Usage Analytics")
        if st.session_state.history:
            df = pd.DataFrame(st.session_state.history)
            feature_counts = df["feature"].value_counts().reset_index()
            feature_counts.columns = ["Feature", "Count"]
            fig = px.bar(feature_counts, x="Feature", y="Count", title="Feature Usage")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No activity yet. Start using the tools to see analytics.")
        st.markdown("</div>", unsafe_allow_html=True)

        if file_text:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            st.markdown("### \U0001F4C4 Uploaded File Preview")
            st.text_area("Extracted Text", file_text[:3000], height=250)
            st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("### \U0001F558 Recent Activity")
        if st.session_state.history:
            for item in reversed(st.session_state.history[-5:]):
                st.markdown(
                    f"<div class='history-box'><b>{item['feature']}</b><br><small>{item['timestamp']}</small></div>",
                    unsafe_allow_html=True
                )
        else:
            st.caption("No recent activity.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("### \U0001F4CC Last Output Preview")
        if st.session_state.last_output:
            preview = str(st.session_state.last_output)[:500]
            st.text_area("Last Output", preview, height=200)
        else:
            st.caption("No output generated yet.")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "\U0001F4AC AI Chat Assistant":
    st.subheader("\U0001F4AC AI Chat Assistant")
    user_prompt = st.text_area("Enter your academic question:")

    if st.button("\U0001F680 Get AI Response"):
        if user_prompt.strip():
            response = get_chatbot_response(user_prompt)
            st.session_state.last_output = response
            st.write(response)
            add_history("AI Chat", user_prompt, response)
        else:
            st.warning("Please enter a question.")

elif menu == "\U0001F4DD Summarizer":
    st.subheader("\U0001F4DD Smart Summarizer")
    text_input = st.text_area("Paste notes/text here:", value=file_text)

    if st.button("\U0001F4CC Summarize"):
        if text_input.strip():
            summary = summarize_text(text_input)
            st.session_state.last_output = summary
            st.write(summary)
            add_history("Summarizer", text_input[:500], summary)
        else:
            st.warning("Please enter text to summarize.")

elif menu == "\u2753 Quiz Generator":
    st.subheader("\u2753 Quiz Generator")
    quiz_input = st.text_area("Enter topic or study material:", value=file_text)

    if st.button("\U0001F9E0 Generate Quiz"):
        if quiz_input.strip():
            quiz = generate_quiz(quiz_input)
            st.session_state.last_output = quiz
            st.write(quiz)
            add_history("Quiz Generator", quiz_input[:500], quiz)
        else:
            st.warning("Please enter topic/text.")

elif menu == "\U0001F4DA Answer Generator":
    st.subheader("\U0001F4DA Answer Generator")
    question = st.text_input("Enter question:")
    support_text = st.text_area("Optional supporting notes:", value=file_text)

    if st.button("\u270D\uFE0F Generate Answer"):
        if question.strip():
            answer = generate_answer(question, support_text)
            st.session_state.last_output = answer
            st.write(answer)
            add_history("Answer Generator", question, answer)
        else:
            st.warning("Please enter a question.")

elif menu == "\U0001F511 Keyword Extractor":
    st.subheader("\U0001F511 Keyword Extractor")
    keyword_input = st.text_area("Enter notes/text:", value=file_text)

    if st.button("\U0001F50D Extract Keywords"):
        if keyword_input.strip():
            keywords = extract_keywords(keyword_input)
            st.session_state.last_keywords = keywords
            st.session_state.last_output = ", ".join(keywords)

            st.markdown("### Important Keywords")
            for kw in keywords:
                st.markdown(f"<span class='keyword-chip'>{kw}</span>", unsafe_allow_html=True)

            add_history("Keyword Extractor", keyword_input[:500], ", ".join(keywords))
        else:
            st.warning("Please enter text.")

elif menu == "\U0001F3A8 AI Image Generator":
    st.subheader("\U0001F3A8 AI Image Generator")

    prompt = st.text_input("Enter image prompt:")
    style = st.selectbox(
        "Choose style",
        [
            "Realistic", "Anime", "Cartoon", "Fantasy",
            "Cyberpunk", "3D Render", "Watercolor",
            "Pixel Art", "Studio Ghibli-like"
        ]
    )

    if st.button("\U0001F5BC\uFE0F Generate Image"):
        if prompt.strip():
            with st.spinner("Generating image... please wait"):
                image = generate_image(prompt, style)
                st.image(image, caption=f"{style}: {prompt}", use_container_width=True)

                st.session_state.image_history.append({
                    "timestamp": str(datetime.now()),
                    "prompt": prompt,
                    "style": style
                })

                st.session_state.last_output = f"Image generated: {prompt} ({style})"
                add_history("AI Image Generator", f"{prompt} ({style})", "Image generated")
        else:
            st.warning("Please enter an image prompt.")

    if st.session_state.image_history:
        st.markdown("### \U0001F558 Recent Image Prompts")
        for img_item in reversed(st.session_state.image_history[-5:]):
            st.markdown(
                f"<div class='history-box'><b>{img_item['timestamp']}</b><br>{img_item['prompt']} <i>({img_item['style']})</i></div>",
                unsafe_allow_html=True
            )

elif menu == "\U0001F4DC History & Export":
    st.subheader("\U0001F4DC History & Export")

    search_query = st.text_input("\U0001F50E Search history by feature or input")

    filtered_history = st.session_state.history
    if search_query.strip():
        filtered_history = [
            item for item in st.session_state.history
            if search_query.lower() in item["feature"].lower()
            or search_query.lower() in item["input"].lower()
        ]

    if filtered_history:
        for item in reversed(filtered_history):
            with st.expander(f"{item['timestamp']} • {item['feature']}"):
                st.write("**Input:**", item["input"])
                st.write("**Output:**", item["output"])
    else:
        st.info("No history found.")

    st.markdown("### \U0001F4E4 Export Options")

    json_data = json.dumps(st.session_state.history, indent=4)
    st.download_button(
        label="\u2B07\uFE0F Download History as JSON",
        data=json_data,
        file_name="student_learning_history.json",
        mime="application/json"
    )

    txt_data = export_history_as_txt(st.session_state.history)
    st.download_button(
        label="\u2B07\uFE0F Download History as TXT",
        data=txt_data,
        file_name="student_learning_history.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Built for university student")