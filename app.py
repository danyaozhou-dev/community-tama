import streamlit as st
import time

# --- 1. 32-BIT VISUAL STYLING ---
st.set_page_config(page_title="COMMUNITY TAMA", page_icon="👾")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #58a6ff; font-family: 'Courier New', monospace; }
    .console-border {
        border: 8px solid #30363d;
        padding: 20px;
        background-color: #161b22;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 20px #58a6ff;
    }
    .pixel-text { color: #39FF14; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MULTIPLAYER GLOBAL STATE ---
# In a real app, this would be a database. 
# For now, we use session_state (Shared per server instance)
if 'xp' not in st.session_state:
    st.session_state.xp = 0
if 'hunger' not in st.session_state:
    st.session_state.hunger = 100

# --- 3. THE GAME UI ---
st.markdown('<div class="console-border">', unsafe_allow_html=True)
st.markdown('<h1 class="pixel-text">📟 MULTIPLAYER TAMA</h1>', unsafe_allow_html=True)

# Evolution System
if st.session_state.xp < 50:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1bTh6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKMGpxxX5F3K3Vm/giphy.gif", width=250)
    st.subheader("STAGE: 🥚 BIT-EGG")
elif st.session_state.xp < 200:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1bTh6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/l41lTjJ8z8z8z8z8z8/giphy.gif", width=250)
    st.subheader("STAGE: 👾 NEON-KID")
else:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1bTh6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxbmR6bmIzeHpxJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKVUn7iM8FMEU24/giphy.gif", width=300)
    st.subheader("STAGE: 👑 OMEGA-BYTE")

# Stats Bars
st.write(f"**COMMUNITY XP:** {st.session_state.xp}")
st.progress(min(st.session_state.xp / 300, 1.0))
st.write(f"**HUNGER:** {st.session_state.hunger}%")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. CONTROLS ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    if st.button("🍎 FEED TAMA"):
        st.session_state.xp += 5
        st.session_state.hunger = min(100, st.session_state.hunger + 10)
        st.toast("Yum! +5 XP")
with c2:
    if st.button("🎮 PLAY GAME"):
        st.session_state.xp += 15
        st.session_state.hunger = max(0, st.session_state.hunger - 5)
        st.snow()

# --- 5. BGM ---
st.audio("https://www.soundjay.com/free-music/sounds/iron-man-01.mp3")