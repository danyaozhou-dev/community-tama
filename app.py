import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="TAMA ENGINE", layout="centered")
# Refresh the "Engine" every 2 seconds to move the pet
st_autorefresh(interval=2000, key="gameloop")

st.markdown("""
    <style>
    .stApp { background-color: #222; display: flex; justify-content: center; }
    .tama-shell {
        background: linear-gradient(145deg, #33ccff, #0066ff); /* Blue Shell */
        border: 8px solid #000; border-radius: 120px 120px 100px 100px;
        width: 400px; padding: 50px 30px; text-align: center; box-shadow: 15px 15px 0px #000;
    }
    .tama-screen {
        background-color: #99ad88; border: 6px solid #444;
        height: 300px; position: relative; overflow: hidden; /* Canvas for movement */
        box-shadow: inset 4px 4px 0px #000;
    }
    .pet-sprite {
        position: absolute;
        transition: all 1.5s ease-in-out; /* Smooth movement animation */
        font-size: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ENGINE STATE (Memory) ---
if 'xp' not in st.session_state:
    st.session_state.xp = 0
    st.session_state.pos = [100, 100] # Initial X, Y

# --- 3. ENGINE LOGIC (The Loop) ---
# Randomly move the pet every refresh
st.session_state.pos[0] = random.randint(10, 250) # Random X
st.session_state.pos[1] = random.randint(10, 180) # Random Y

# --- 4. THE HANDHELD DISPLAY ---
st.markdown('<div class="tama-shell">', unsafe_allow_html=True)
st.markdown(f'''
    <div class="tama-screen">
        <div class="pet-sprite" style="left:{st.session_state.pos[0]}px; top:{st.session_state.pos[1]}px;">
            👾
        </div>
    </div>
''', unsafe_allow_html=True)

# GROWTH LOGIC
stage = "EGG" if st.session_state.xp < 50 else "TEEN" if st.session_state.xp < 200 else "GOD"
st.write(f"**{stage}** | XP: {st.session_state.xp}")

# --- 5. MINI-GAME: REFLEX CATCH ---
st.markdown("### 🕹️ MINI-GAME")
if st.button("🎯 CATCH PET!"):
    # If you click while it moves, you get XP
    st.session_state.xp += 15
    st.success("GOTCHA! +15 XP")
    if st.session_state.xp % 50 == 0:
        st.balloons()

st.markdown('</div>', unsafe_allow_html=True)