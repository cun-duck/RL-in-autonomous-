import streamlit as st
import pydeck as pdk
import pandas as pd
from data_handling import prepare_data

# Fungsi untuk menggambar grafik metrik
def render_metrics_chart(data, project, accuracy_weight, collision_weight, time_weight):
    project_data = prepare_data(data, project)
    
    # Misalnya, menggunakan Matplotlib atau Plotly untuk menggambar grafik
    st.write(f"Showing metrics for {project}")
    st.line_chart(project_data[["accuracy", "collision", "time_efficiency"]])

# Fungsi untuk animasi jalur kendaraan
def animate_vehicle_path():
    st.subheader("Simulated Vehicle Path")
    
    # Data jalur kendaraan (contoh)
    vehicle_data = pd.DataFrame({
        "lat": [37.7749, 37.7750, 37.7751, 37.7752],  # Latitude
        "lon": [-122.4194, -122.4193, -122.4192, -122.4191],  # Longitude
        "time": [1, 2, 3, 4]  # Waktu pergerakan kendaraan
    })
    
    # Membuat deck untuk menampilkan peta dengan Pydeck
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=37.775, longitude=-122.4194, zoom=15),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",  # Jenis layer yang digunakan untuk menampilkan titik kendaraan
                data=vehicle_data,  # Data jalur kendaraan
                get_position=["lon", "lat"],  # Mendapatkan posisi titik berdasarkan longitude dan latitude
                get_color=[255, 0, 0],  # Warna titik kendaraan (merah)
                get_radius=200,  # Ukuran titik
                radius_min_pixels=5,  # Ukuran minimal titik
                radius_max_pixels=10,  # Ukuran maksimal titik
                pickable=True,  # Memungkinkan interaksi dengan titik
            ),
        ],
        tooltip={"text": "{time}"}  # Menampilkan waktu ketika titik kendaraan diklik
    )
    
    # Menampilkan peta dengan Streamlit
    st.pydeck_chart(deck)
