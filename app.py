import streamlit as st
import numpy as np
import cv2
import random
import time

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
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #d0d0d0;
        margin-bottom: 25px;
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }

    .footer {
        text-align: center;
        color: #bbbbbb;
        margin-top: 30px;
        font-size: 14px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #ff512f, #dd2476);
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #dd2476, #ff512f);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🎯 Gesture-Controlled Shooting Game</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Cloud Demo Mode • Full hand-tracking version runs locally</div>',
    unsafe_allow_html=True
)

# ---------------- GAME SETTINGS ----------------
WIDTH, HEIGHT = 960, 540
PLAYER_W, PLAYER_H = 120, 20
ENEMY_SIZE = 40

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "enemy_y" not in st.session_state:
    st.session_state.enemy_y = 0
if "enemy_x" not in st.session_state:
    st.session_state.enemy_x = random.randint(50, WIDTH - 50)
if "last_time" not in st.session_state:
    st.session_state.last_time = time.time()

# ---------------- LAYOUT ----------------
left, center, right = st.columns([1.2, 2.6, 1.2])

# ---------------- LEFT PANEL ----------------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🕹 Controls")
    st.markdown("""
    • Slider → Move shooter  
    • Button → Fire  
    • Hit enemy → +10 score  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:15px"></div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Note")
    st.markdown("""
    Webcam & MediaPipe are disabled  
    on Streamlit Cloud.

    Local version uses  
    **real hand gestures**.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CENTER GAME AREA ----------------
with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    frame_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

    fire = st.button("🔥 Fire")

# ---------------- RIGHT PANEL ----------------
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎯 Settings")
    player_x_ratio = st.slider("Move Player", 0.0, 1.0, 0.5)
    difficulty = st.slider("Enemy Speed", 3, 10, 5)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:15px"></div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏆 Score")
    st.markdown(f"### {st.session_state.score}")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- GAME LOGIC ----------------
frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
frame[:] = (20, 20, 40)

# player
player_x = int(player_x_ratio * WIDTH)
player_x = max(PLAYER_W//2, min(WIDTH - PLAYER_W//2, player_x))
player_y = HEIGHT - 60

cv2.rectangle(
    frame,
    (player_x - PLAYER_W//2, player_y),
    (player_x + PLAYER_W//2, player_y + PLAYER_H),
    (200, 200, 200),
    -1
)

# enemy movement
now = time.time()
if now - st.session_state.last_time > 0.03:
    st.session_state.enemy_y += difficulty
    st.session_state.last_time = now

if st.session_state.enemy_y > HEIGHT:
    st.session_state.enemy_y = 0
    st.session_state.enemy_x = random.randint(50, WIDTH - 50)

# draw enemy
ex = st.session_state.enemy_x
ey = st.session_state.enemy_y
cv2.rectangle(
    frame,
    (ex, ey),
    (ex + ENEMY_SIZE, ey + ENEMY_SIZE),
    (0, 0, 255),
    -1
)

# fire collision
if fire:
    if abs(player_x - (ex + ENEMY_SIZE//2)) < 60 and ey > 100:
        st.session_state.score += 10
        st.session_state.enemy_y = 0
        st.session_state.enemy_x = random.randint(50, WIDTH - 50)

# draw score text
cv2.putText(
    frame,
    f"Score: {st.session_state.score}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# show frame
frame_placeholder.image(frame, channels="BGR")

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built by Tejas Narkhede • Computer Vision Game Project</div>',
    unsafe_allow_html=True
)
