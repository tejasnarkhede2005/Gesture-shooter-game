import streamlit as st
from game import run_game

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gesture Shooter Game",
    page_icon="🎯",
    layout="wide",
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Title */
    .title-text {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
        color: #ffffff;
    }

    /* Subtitle */
    .subtitle-text {
        font-size: 18px;
        text-align: center;
        color: #d0d0d0;
        margin-bottom: 30px;
    }

    /* Card */
    .card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #ff512f, #dd2476);
        color: white;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        transition: transform 0.1s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #dd2476, #ff512f);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #bbbbbb;
        margin-top: 30px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown('<div class="title-text">🎯 Gesture-Controlled Shooting Game</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Move your index finger to aim • Pinch to shoot • Survive as long as possible</div>',
    unsafe_allow_html=True
)

# ---------------- LAYOUT ----------------
left, center, right = st.columns([1.2, 2.6, 1.2])

# ---------------- LEFT PANEL ----------------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🕹 Controls")
    st.markdown("""
    • Move **index finger** → Move shooter  
    • **Pinch (thumb + index)** → Fire bullet  
    • Avoid enemies  
    • Score increases on hit  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:15px"></div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎮 Game Info")
    st.markdown("""
    • Real-time hand tracking  
    • No keyboard or mouse  
    • Built using OpenCV + MediaPipe  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CENTER GAME AREA ----------------
with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    frame_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

    start = st.button("▶ Start Game")

# ---------------- RIGHT PANEL ----------------
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚙ Settings")
    difficulty = st.slider("Enemy Spawn Speed", 0.5, 2.0, 1.0, 0.1)
    st.caption("Lower = easier, Higher = harder")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:15px"></div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Notes")
    st.markdown("""
    Streamlit version runs at lower FPS  
    for stability on web platforms.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RUN GAME ----------------
if start:
    run_game(frame_placeholder)

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built by Tejas Narkhede • Computer Vision Game Project</div>',
    unsafe_allow_html=True
)
