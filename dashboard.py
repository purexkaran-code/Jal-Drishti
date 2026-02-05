import streamlit as st
import pandas as pd
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jal-Drishti Command Center",
    page_icon="🌊",
    layout="wide"  # Uses the whole screen width
)

# --- SIDEBAR (The Manual) ---
with st.sidebar:
    st.header("📘 Control Panel")
    st.markdown("### System Status: **ONLINE**")
    
    # Load the manual
    try:
        with open("flood_guidelines.txt", "r") as f:
            safety_manual = f.read()
    except FileNotFoundError:
        safety_manual = "Protocol B-12: Evacuate to high ground."
        
    st.info(f"**Current Protocol:**\n\n{safety_manual}")
    st.write("---")
    st.caption("Powered by Pathway & OpenAI")

# --- MAIN DASHBOARD ---
st.title("🌊 Jal-Drishti: Urban Flood Monitor")

# Create 3 columns for big stats
col1, col2, col3 = st.columns(3)

# Placeholders for the big numbers
with col1:
    level_metric = st.empty()
with col2:
    status_metric = st.empty()
with col3:
    trend_metric = st.empty()

st.divider() # A nice visual line

# Placeholder for the main chart
st.subheader("Real-Time Water Levels (Sector 4)")
chart_holder = st.empty()

# Placeholder for the BIG RED ALERT
alert_box = st.empty()

while True:
    try:
        # Read data
        data = pd.read_csv("water_data.csv")
        
        if not data.empty:
            current_level = data.iloc[-1]["water_level"]
            
            # Calculate "Rate of Rise" (Current - Previous)
            if len(data) > 1:
                prev_level = data.iloc[-2]["water_level"]
                change = current_level - prev_level
            else:
                change = 0

            # --- UPDATE THE METRICS ---
            level_metric.metric(label="Water Level", value=f"{current_level:.1f} cm", delta=f"{change:.2f} cm")
            
            # --- COLOR LOGIC ---
            if current_level > 45:
                status_metric.metric(label="Status", value="CRITICAL", delta_color="inverse")
                trend_metric.error("⚠️ EVACUATE")
                
                # Show the Area Chart (Looks like water)
                chart_holder.area_chart(data["water_level"], color="#ff4b4b") # Red water
                
                # Big Alert Message
                alert_box.error(f"🚨 FLASH FLOOD DETECTED! \n\nAI ADVICE: {safety_manual}")
                
            else:
                status_metric.metric(label="Status", value="Normal")
                trend_metric.success("✅ SAFE")
                
                # Show Blue Water
                chart_holder.area_chart(data["water_level"], color="#0000FF") 
                
                alert_box.empty() # Clear the alert if safe

    except Exception as e:
        time.sleep(0.5)
        
    time.sleep(1)