import streamlit as st
import time
import json
import os

# --- FILE DATABASE SYSTEM ---
# This ensures everyone interacts with the SAME pet data
DB_FILE = "tamagotchi_state.json"

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "Cyber-Tama",
        "hunger": 100,
        "happiness": 100,
        "last_tick": time.time(),
        "xp": 0,
        "leaderboard": {}
    }

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

# --- GAME LOGIC ---
data = load_data()

# Real-time Decay (2 points per minute)
elapsed_minutes = (time.time() - data["last_tick"]) / 60
data["hunger"] = max(0, data["hunger"] - (elapsed_minutes * 2))
data["happiness"] = max(0, data["happiness"] - (elapsed_minutes * 1.5))
data["last_tick"] = time.time()

# --- WEB UI ---
st.set_page_config(page_title="Community Tamagotchi", page_icon="📟")
st.title(f"📟 {data['name']}'s World")

# Evolution Logic
stage = "🥚 Egg"
if data["xp"] > 100: stage = "🐣 Chick"
if data["xp"] > 500: stage = "🦕 Dino"
if data["xp"] > 1000: stage = "👑 God-Zilla"

# Display Stats
col1, col2, col3 = st.columns(3)
col1.metric("Hunger", f"{int(data['hunger'])}%")
col2.metric("Happiness", f"{int(data['happiness'])}%")
col3.metric("Stage", stage)

# Progress bars for visual flair
st.progress(data["hunger"] / 100)

# --- USER INTERACTION ---
user_name = st.text_input("Enter your name to play:", "Guest")

c1, c2 = st.columns(2)
if c1.button("🍎 Feed (Full Meal)"):
    data["hunger"] = min(100, data["hunger"] + 20)
    data["xp"] += 10
    data["leaderboard"][user_name] = data["leaderboard"].get(user_name, 0) + 10
    save_data(data)
    st.success(f"{user_name} fed the pet!")

if c2.button("🎾 Play (Game)"):
    data["happiness"] = min(100, data["happiness"] + 20)
    data["xp"] += 15
    data["leaderboard"][user_name] = data["leaderboard"].get(user_name, 0) + 15
    save_data(data)
    st.balloons()

# --- LEADERBOARD ---
st.divider()
st.subheader("🏆 Caretaker Leaderboard")
sorted_board = sorted(data["leaderboard"].items(), key=lambda x: x[1], reverse=True)
for i, (player, score) in enumerate(sorted_board[:5]):
    st.write(f"{i+1}. **{player}**: {score} XP")

save_data(data) # Final save for decay updates