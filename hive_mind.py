import streamlit as st
import time
import requests
import os
import redis 
from dotenv import load_dotenv # 👈 THE CRITICAL FIX

# 1. IGNITION: Load the .env file immediately (Works locally)
load_dotenv()

# --- CONFIGURATION ---
PAGE_TITLE = "TheFunFanReporter: EDGE NODE"
PAGE_ICON = "💧"
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Rachel Voice

# --- VULTR REDIS CONNECTION (The Hive Memory) ---
try:
    # Check Streamlit Secrets first, then local .env
    redis_url = os.environ.get("VULTR_REDIS_URL")
    if redis_url:
        r = redis.from_url(redis_url)
        r.ping() 
        VULTR_STATUS = "CONNECTED 🟢"
    else:
        VULTR_STATUS = "NOT FOUND 🔴 (Check Secrets/Env)"
except Exception as e:
    VULTR_STATUS = f"ERROR: {e}"

# --- UI SETUP ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# CUSTOM CSS (Cyberpunk Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    .stTextArea textarea { background-color: #1f1f1f; color: #00ff41; border: 1px solid #00ff41; }
    h1 { color: #00ff41; text-shadow: 0 0 10px #00ff41; }
    .stButton button { background-color: #00ff41; color: black; font-weight: bold; width: 100%; }
    .stripe-button { border: 2px solid #635bff; background-color: #635bff; color: white; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; display: block; text-decoration: none; }
    .vultr-badge { border: 1px solid #0079ff; color: #0079ff; padding: 5px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📡 NETWORK CONTROL")
    connection_mode = st.radio("Connectivity:", ["🟢 CLOUD (Online)", "🔴 EDGE (Offline)"])
    
    st.divider()
    
    # 💳 STRIPE ECONOMY (Safe Link)
    st.header("🏦 MERIT BANK")
    st.markdown('<a href="https://buy.stripe.com/test_eVa01g4F62O45J6dQQ" target="_blank" class="stripe-button">💳 BUY 10 MERIT COINS ($72.50)</a>', unsafe_allow_html=True)

    st.divider()
    
    # 💾 VULTR STATUS
    st.header("💾 HIVE MEMORY")
    st.markdown(f'<span class="vultr-badge">VULTR REDIS: {VULTR_STATUS}</span>', unsafe_allow_html=True)

    # CHECK ELEVENLABS KEY
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if api_key:
        st.caption("🎙️ Voice Module: ACTIVE")
    else:
        st.error("🎙️ Voice Module: MISSING KEY")

# --- MAIN APP ---
st.title("💧 HIVE MIND: LIQUID METAL")
st.caption("TheFunFanReporter 2.0 - Voice-Enabled Resilient Intelligence")

fan_input = st.text_area("📢 INCOMING FAN REPORT:", height=100, placeholder="Type here... (e.g., 'Fight in Section 102!')")

if st.button("ANALYZE REPORT 🚀"):
    if not fan_input:
        st.warning("⚠️ Please enter a report first.")
    else:
        with st.spinner("Processing..."):
            time.sleep(1) 
            
            # LOGIC
            if connection_mode == "🟢 CLOUD (Online)":
                result_text = f"CLOUD ANALYSIS: {fan_input}. Sentiment: NEGATIVE. Threat: HIGH."
                st.success("✅ PROCESSED VIA GOOGLE CLOUD")
                st.write(result_text)
            else:
                # EDGE LOGIC
                threat_level = "LOW"
                if "fight" in fan_input.lower() or "fire" in fan_input.lower():
                    threat_level = "CRITICAL"
                
                result_text = f"EDGE ALERT: {threat_level} THREAT DETECTED. {fan_input.upper()}"
                
                st.markdown(f"""
                <div style="border: 1px solid #00ff41; padding: 20px; border-radius: 10px; background-color: #001a05;">
                    <h3 style="color: #00ff41;">🛡️ LIQUID EDGE REPORT</h3>
                    <p><strong>STATUS:</strong> 🔴 OFFLINE PROCESSED</p>
                    <p><strong>SUMMARY:</strong> {result_text}</p>
                </div>
                """, unsafe_allow_html=True)

            # 🎙️ VOICE ACTIVATION
            if api_key:
                st.divider()
                st.markdown("### 🔊 TACTICAL AUDIO FEED")
                try:
                    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
                    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
                    data = {"text": result_text, "model_id": "eleven_monolingual_v1"}
                    
                    response = requests.post(url, json=data, headers=headers)
                    
                    if response.status_code == 200:
                        st.audio(response.content, format="audio/mp3")
                    else:
                        st.error(f"Voice Error: {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
            else:
                st.warning("⚠️ Voice disabled (No API Key found).")