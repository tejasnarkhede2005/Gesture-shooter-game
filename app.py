import sys
import streamlit as st

st.write(sys.version)
from game import run_game



st.set_page_config(page_title="Gesture Shooter Game", layout="wide")

st.title("🎯 Gesture-Controlled Shooting Game")
st.write("Use your index finger to move. Pinch to shoot.")

start = st.button("▶ Start Game")

frame_placeholder = st.empty()

if start:
    run_game(frame_placeholder)
