# visualization.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_metrics_chart(data, project, accuracy_weight, collision_weight, time_weight):
    st.subheader(f"Algorithm Performance Comparison for {project}")
    
    # Compute weighted metrics
    labels = list(data.keys())
    metrics = [np.array(values) for values in data.values()]
    weighted_metrics = [
        metric * np.array([accuracy_weight, collision_weight, time_weight]) for metric in metrics
    ]

    # Plot bar chart for weighted metrics
    x = np.arange(3)  # Accuracy, Collision Avoidance, Time
    width = 0.2

    fig, ax = plt.subplots()
    for i, (metric, label) in enumerate(zip(weighted_metrics, labels)):
        ax.bar(x + i * width, metric, width, label=label)

    ax.set_xlabel("Metrics")
    ax.set_title("Weighted Comparison of Selected Algorithms")
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(["Path Accuracy", "Collision Avoidance", "Time Efficiency"])
    ax.legend()

    st.pyplot(fig)

def display_summary(project, algorithms):
    # Display detailed summary for each selected algorithm
    st.subheader("Project Summary and Algorithm Insights")
    if project == "CARLA Simulation":
        summary = {
            "PPO": "Excels in path accuracy, balanced in other metrics.",
            "DQN": "Good for collision avoidance, moderate path accuracy.",
            "TD3": "High efficiency in time, with lower path accuracy."
        }
    elif project == "AirSim Simulation":
        summary = {
            "SAC": "Strong path accuracy, efficient in time management.",
            "TRPO": "Superior in collision avoidance but moderate in other areas."
        }
    
    for alg in algorithms:
        st.write(f"**{alg}:** {summary.get(alg, 'No data available')}")
