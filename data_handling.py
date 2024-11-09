# data_handling.py
import pandas as pd

def load_data(project, algorithms):
    # Sample data structure based on selected project and algorithms
    # For real application, load from CSV or database
    data = {
        "CARLA Simulation": {
            "PPO": [85, 95, 70],
            "DQN": [90, 80, 75],
            "TD3": [78, 85, 68]
        },
        "AirSim Simulation": {
            "SAC": [88, 92, 78],
            "TRPO": [82, 87, 74]
        }
    }
    # Filter selected algorithms
    return {alg: data[project][alg] for alg in algorithms if alg in data[project]}
