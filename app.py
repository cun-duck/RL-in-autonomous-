# app.py
import streamlit as st
from data_handling import load_data
from visualization import render_metrics_chart, display_summary

st.title("Comparative Study of RL Algorithms in Autonomous Vehicle Simulations")

# Sidebar for Project and Algorithm Selection
project = st.sidebar.selectbox("Select Project", ["CARLA Simulation", "AirSim Simulation"])
algorithms = st.sidebar.multiselect(
    "Select Algorithms to Compare", 
    ["PPO", "DQN", "TD3", "SAC", "TRPO"], 
    default=["PPO", "DQN"] if project == "CARLA Simulation" else ["SAC", "TRPO"]
)

# Data and Metrics Load
data = load_data(project, algorithms)
st.sidebar.markdown("Adjust Metric Weightings (for Custom Comparison)")

# Sliders for weighting metrics dynamically
accuracy_weight = st.sidebar.slider("Path Accuracy Weight", 0.0, 1.0, 0.5)
collision_weight = st.sidebar.slider("Collision Avoidance Weight", 0.0, 1.0, 0.5)
time_weight = st.sidebar.slider("Time Efficiency Weight", 0.0, 1.0, 0.5)

# Render charts
render_metrics_chart(data, project, accuracy_weight, collision_weight, time_weight)

# Display summary
display_summary(project, algorithms)
