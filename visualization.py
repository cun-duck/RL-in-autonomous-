import pygame
import pandas as pd
import streamlit as st
import time
from io import BytesIO

def animate_vehicle_path(data, project):
    # Load the data for the selected project
    project_data = data[project]
    
    # Extract the lat, lon, and time columns
    vehicle_data = project_data[['time', 'lat', 'lon']]

    # Initialize Pygame
    pygame.init()
    
    # Set the window size
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Vehicle Path Animation - {project}")
    
    # Set up the clock for frame rate
    clock = pygame.time.Clock()
    
    # Scaling factor for lat/lon to fit within the window
    lat_scale = 50000
    lon_scale = 50000

    # Initial position of the vehicle (start with the first data point)
    vehicle_pos = [vehicle_data['lon'].iloc[0] * lon_scale, vehicle_data['lat'].iloc[0] * lat_scale]
    vehicle_radius = 10

    # Vehicle color (Red)
    vehicle_color = (255, 0, 0)
    
    # Set the background color
    background_color = (255, 255, 255)

    # Run the animation loop
    for index, row in vehicle_data.iterrows():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen and set the background color
        screen.fill(background_color)

        # Update the vehicle position
        vehicle_pos = [row['lon'] * lon_scale, row['lat'] * lat_scale]

        # Draw the vehicle as a red circle
        pygame.draw.circle(screen, vehicle_color, (int(vehicle_pos[0]), int(vehicle_pos[1])), vehicle_radius)

        # Update the screen
        pygame.display.flip()

        # Wait before showing the next frame (adjust time as needed)
        time.sleep(0.1)

        # Limit the frame rate (optional)
        clock.tick(30)

    pygame.quit()

    # Convert the final frame to an image for Streamlit display
    img_bytes = pygame.image.tostring(screen, "RGB")
    img = pygame.image.load(BytesIO(img_bytes))
    st.image(img)
