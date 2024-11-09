import pandas as pd

# Fungsi untuk memuat data (misalnya dari CSV atau sumber lain)
def load_data():
    # Contoh memuat data dari file CSV
    data = {
        "Project A": pd.read_csv("project_a_data.csv"),
        "Project B": pd.read_csv("project_b_data.csv"),
    }
    return data

# Fungsi untuk menyiapkan data berdasarkan proyek yang dipilih
def prepare_data(data, project):
    # Mempersiapkan data, bisa meliputi pembersihan atau transformasi
    project_data = data[project]
    # Misalnya, membersihkan data atau menyiapkan metrik tertentu
    return project_data
