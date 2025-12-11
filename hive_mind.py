import streamlit as st
import time
import random

# --- CONFIGURATION ---
# This is the "Liquid Metal" Edition
PAGE_TITLE = "TheFunFanReporter: EDGE NODE"
PAGE_ICON = "💧"

# --- UI SETUP ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# CUSTOM CSS (Neon Green & Silver for "Liquid" Vibe)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    .stTextArea textarea { background-color: #1f1f1f; color: #00ff41; border: 1px solid #00ff41; }
    h1 { color: #00ff41; text-shadow: 0 0 10px #00ff41; }
    .stButton button { background-color: #00ff41; color: black; font-weight: bold; }
    .edge-badge { border: 2px solid #00ff41; padding: 5px 10px; border-radius: 5px; color: #00ff41; font-weight: bold; }
    .cloud-badge { border: 2px solid #00d4ff; padding: 5px 10px; border-radius: 5px; color: #00d4ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: THE "KILL SWITCH" ---
with st.sidebar:
    st.title("📡 NETWORK CONTROL")
    st.info("Simulate Internet Outage for Liquid Metal Demo")
    
    # The Switch
    connection_mode = st.radio("Connectivity:", ["🟢 CLOUD (Online)", "🔴 EDGE (Offline)"])
    
    st.divider()
    if connection_mode == "🟢 CLOUD (Online)":
        st.markdown('<span class="cloud-badge">CONNECTED TO GOOGLE VERTEX</span>', unsafe_allow_html=True)
        st.metric("Latency", "45ms")
    else:
        st.markdown('<span class="edge-badge">RUNNING ON LOCAL LIQUID NODE</span>', unsafe_allow_html=True)
        st.metric("Latency", "0.5ms", "⚡ SUPER FAST")

# --- MAIN APP ---
st.title("💧 HIVE MIND: LIQUID METAL")
st.caption("TheFunFanReporter 2.0 - Resilient Crowd Intelligence")

# 1. THE INPUT
fan_input = st.text_area("📢 INCOMING FAN REPORT:", height=100, placeholder="Type here... (e.g., 'Fight in Section 102!')")

# 2. THE LOGIC
if st.button("ANALYZE REPORT 🚀"):
    if not fan_input:
        st.warning("⚠️ Please enter a report first.")
    else:
        with st.spinner("Processing..."):
            time.sleep(1) # Dramatic pause
            
            # --- SCENARIO A: CLOUD MODE (Google) ---
            if connection_mode == "🟢 CLOUD (Online)":
                # In a real app, this calls Vertex AI. 
                # For the demo, we simulate the AI response to save API costs during testing.
                st.success("✅ PROCESSED VIA CLOUD")
                st.markdown(f"**☁️ GOOGLE AI SAYS:** Alert received. Analyzing '{fan_input}' for sentiment and threat level...")
            
            # --- SCENARIO B: EDGE MODE (Liquid Metal) ---
            else:
                # This is the WINNING FEATURE. 
                # It works without internet using simple Python logic (Edge AI).
                
                # Simple Keyword Detection (The "Tiny Brain")
                threat_level = "LOW"
                action = "Monitor Situation"
                
                if "fight" in fan_input.lower() or "gun" in fan_input.lower() or "fire" in fan_input.lower():
                    threat_level = "CRITICAL"
                    action = "DISPATCH SECURITY TEAM ALPHA"
                elif "beer" in fan_input.lower() or "drunk" in fan_input.lower():
                    threat_level = "MEDIUM"
                    action = "Send Staff to De-escalate"
                
                st.markdown(f"""
                <div style="border: 1px solid #00ff41; padding: 20px; border-radius: 10px; background-color: #001a05;">
                    <h3 style="color: #00ff41;">🛡️ LIQUID EDGE REPORT</h3>
                    <p><strong>STATUS:</strong> 🔴 OFFLINE PROCESSED</p>
                    <p><strong>THREAT LEVEL:</strong> {threat_level}</p>
                    <p><strong>ACTION REQUIRED:</strong> {action}</p>
                    <p><em>Data saved to local Liquid Memory. Syncing when online...</em></p>
                </div>
                """, unsafe_allow_html=True)