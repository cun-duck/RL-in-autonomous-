import streamlit as st
import pydeck as pdk
import pandas as pd
import time

def render_metrics_chart(data, project, accuracy_weight, collision_weight, time_weight):
    """
    Render a chart of algorithm performance metrics with the given weights.
    """
    # Prepare data for metrics chart
    project_data = data[project]
    accuracy = project_data["accuracy"] * accuracy_weight
    collision_avoidance = project_data["collision_avoidance"] * collision_weight
    time_efficiency = project_data["time_efficiency"] * time_weight
    
    # Create a DataFrame for the metrics
    metrics_data = pd.DataFrame({
        "Metric": ["Accuracy", "Collision Avoidance", "Time Efficiency"],
        "Score": [accuracy.sum(), collision_avoidance.sum(), time_efficiency.sum()]
    })
    
    st.write("Performance Metrics:")
    st.bar_chart(metrics_data.set_index('Metric'))

def animate_vehicle_path(data, project):
    """
    Render the vehicle path animation on a map using Pydeck, with looping animation.
    """
    # Load project data
    project_data = data[project]

    # Prepare data for the vehicle path animation
    vehicle_data = project_data[["lat", "lon", "time"]]
    
    # Create a pydeck layer to display vehicle paths
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=vehicle_data["lat"].mean(),
                                         longitude=vehicle_data["lon"].mean(),
                                         zoom=15),
        layers=[
            pdk.Layer(
                "PathLayer",  # Layer for drawing paths
                data=vehicle_data,  # Data for vehicle path
                get_path="[[lon, lat]]",  # Coordinates for the path
                get_width=5,  # Path width
                get_color=[0, 255, 0],  # Path color (green)
                width_min_pixels=2,
                pickable=True,  # Enable interactions
                opacity=0.7  # Path opacity
            ),
        ],
        tooltip={"text": "{time}"},  # Tooltip to show time on hover
    )

    # Display the pydeck map in Streamlit
    st.pydeck_chart(deck)

    # Looping animation for vehicle movement over time
    st.write("Vehicle Path Animation with Looping")
    
    # Loop through the vehicle path data for animation
    i = 0
    while True:
        if i >= len(vehicle_data):  # Reset the loop after completing one cycle
            i = 0  # Restart the animation from the beginning
        
        # Get the current position of the vehicle
        current_position = vehicle_data.iloc[i]
        
        # Display the current step and vehicle's location
        st.write(f"Step {i+1}: Vehicle is at ({current_position['lat']}, {current_position['lon']})")
        
        # Update the pydeck chart with the new position (animation effect)
        deck = pdk.Deck(
            initial_view_state=pdk.ViewState(latitude=current_position["lat"],
                                             longitude=current_position["lon"],
                                             zoom=15),
            layers=[
                pdk.Layer(
                    "PathLayer",
                    data=vehicle_data.iloc[:i+1],  # Show the path up to the current position
                    get_path="[[lon, lat]]",
                    get_width=5,
                    get_color=[0, 255, 0],
                    width_min_pixels=2,
                    pickable=True,
                    opacity=0.7,
                ),
            ],
            tooltip={"text": f"Step {i+1}: {current_position['time']}"},  # Tooltip with time
        )
        
        # Display updated chart
        st.pydeck_chart(deck)
        
        # Simulate time delay for animation effect
        time.sleep(1)  # Delay for 1 second between updates
        
        # Move to the next step
        i += 1
