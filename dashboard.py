import streamlit as st
import pandas as pd
import time
from google import genai

# --- CONFIGURATION ---
# Paste your API key inside the quotes below!
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="Jal-Drishti Command Center", page_icon="🌊", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.header("📘 Control Panel")
    st.markdown("### System Status: **ONLINE**")
    try:
        with open("flood_guidelines.txt", "r") as f:
            safety_manual = f.read()
    except FileNotFoundError:
        safety_manual = "Protocol B-12: Evacuate to high ground."
    st.info(f"**Knowledge Base (NDMA):**\n\n{safety_manual}")

# --- MAIN DASHBOARD ---
st.title("🌊 Jal-Drishti: AI Flood Monitor")

col1, col2, col3 = st.columns(3)
with col1:
    level_metric = st.empty()
with col2:
    status_metric = st.empty()
with col3:
    trend_metric = st.empty()

st.divider()

left_col, right_col = st.columns(2)
with left_col:
    st.subheader("Real-Time Water Levels")
    chart_holder = st.empty()
    alert_box = st.empty()
with right_col:
    st.subheader("Live Sector Map (Sector 4)")
    map_holder = st.empty()

map_data = pd.DataFrame({'lat': [28.6139], 'lon': [77.2090]})

current_ai_message = None 

while True:
    try:
        data = pd.read_csv("water_data.csv")
        
        if not data.empty:
            current_level = data.iloc[-1]["water_level"]
            change = current_level - data.iloc[-2]["water_level"] if len(data) > 1 else 0

            level_metric.metric(label="Water Level", value=f"{current_level:.1f} cm", delta=f"{change:.2f} cm")
            
            if current_level > 45:
                status_metric.metric(label="Status", value="CRITICAL", delta_color="inverse")
                trend_metric.error("⚠️ EVACUATE")
                chart_holder.line_chart(data["water_level"], color="#ff4b4b")
                map_holder.map(map_data, size=2000, color="#ff0000") 
                
                # --- THE NEW RAG AI BRAIN ---
                if current_ai_message is None:
                    prompt = f"You are an emergency AI. Water level is {current_level:.1f}cm. Read manual: '{safety_manual}'. Write a 2-sentence evacuation command for Sector 4 based ONLY on the manual."
                    try:
                        # Using the new Google GenAI syntax!
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=prompt
                        )
                        current_ai_message = response.text
                    except Exception as e:
                        current_ai_message = "AI connection error. Evacuate immediately based on manual protocols."
                
                alert_box.error(f"🚨 LIVE AI EVACUATION PROTOCOL:\n\n**{current_ai_message}**")
                
            else:
                status_metric.metric(label="Status", value="Normal")
                trend_metric.success("✅ SAFE")
                chart_holder.line_chart(data["water_level"], color="#0000FF")
                map_holder.map(map_data, size=100, color="#0044ff")
                
                current_ai_message = None 
                alert_box.empty()

    except Exception as e:
            st.error(f"System Error: {e}")
            time.sleep(1)
    time.sleep(1)
    #run cmd: streamlit run dashboard.py
