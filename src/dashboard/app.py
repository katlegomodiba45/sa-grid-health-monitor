import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
sys.path.append(".")

from src.ingestion.fetch_weather import fetch_weather
from src.ingestion.fetch_grid import fetch_grid_status
from src.model.stress_score import calculate_stress_score, stress_label

st.set_page_config(page_title="SA Grid Resilience Monitor", page_icon="⚡", layout="wide")

st.title("⚡ SA Grid Resilience & Health Monitor")
st.caption("Public data • Transparent scoring • Portfolio project")

with st.spinner("Fetching latest data..."):
    try:
        weather_df = fetch_weather()
        grid_df = fetch_grid_status()
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

st.write(f"**Last updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")

st.header("1. Current Grid Status")
status = grid_df.iloc[0]["status"]
stage = grid_df.iloc[0].get("stage")

if status == "TOKEN_MISSING":
    st.warning("Add your EskomSePush token in a .env file as ESKOM_TOKEN")
    current_stage = None
else:
    current_stage = stage
    st.metric("National Stage", current_stage if current_stage is not None else "Unknown")

st.header("2. Weather – Major Cities")
st.dataframe(weather_df[["city", "temperature_c", "humidity_percent", "wind_speed_kmh"]], use_container_width=True)

fig = px.bar(weather_df, x="city", y="temperature_c", title="Temperature by City", color="temperature_c", color_continuous_scale="OrRd")
st.plotly_chart(fig, use_container_width=True)

st.header("3. Grid Stress Score")
jhb_temp = weather_df.loc[weather_df["city"] == "Johannesburg", "temperature_c"]
temp = float(jhb_temp.values[0]) if not jhb_temp.empty else None
hour = (datetime.utcnow().hour + 2) % 24

score = calculate_stress_score(current_stage, temp, hour)
label = stress_label(score)

col1, col2 = st.columns(2)
col1.metric("Stress Score", f"{score}/100")
col2.metric("Risk Level", label)

st.info("Score is based on stage + temperature + time of day. Transparent rules, not a prediction model.")
st.caption("Built by Katlego Modiba • Not an official Eskom tool")