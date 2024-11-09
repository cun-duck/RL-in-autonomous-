import streamlit as st
import pandas as pd
from data_handling import load_data
from visualization import render_metrics_chart, animate_vehicle_path

# Sidebar configuration
st.sidebar.header("Autonomous Driving Algorithm Comparison")

# Load data
data = load_data()

# Prepare data based on user input
project = st.sidebar.selectbox("Select Project", data.keys())
accuracy_weight = st.sidebar.slider("Accuracy Weight", 0.0, 1.0, 0.3)
collision_weight = st.sidebar.slider("Collision Avoidance Weight", 0.0, 1.0, 0.4)
time_weight = st.sidebar.slider("Time Efficiency Weight", 0.0, 1.0, 0.3)

# Display project overview
st.title(f"Comparing Reinforcement Learning Algorithms for {project}")
st.write("Explore the performance of different algorithms with various weights.")

# Show metrics chart with animation
render_metrics_chart(data, project, accuracy_weight, collision_weight, time_weight)

# Display path animation for vehicle
animate_vehicle_path(data, project)
