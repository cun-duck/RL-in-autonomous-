import pandas as pd

def load_data():
    """
    Load the project data from CSV files and return them in a dictionary.
    The dictionary keys will be the project names, and values will be the dataframes.
    """
    # Load the data for each project
    project_a_data = pd.read_csv("project_a_data.csv")
    project_b_data = pd.read_csv("project_b_data.csv")
    
    # Create a dictionary to store the dataframes
    data = {
        "Project A": project_a_data,
        "Project B": project_b_data
    }
    
    return data

def prepare_data(data, project_name):
    """
    Prepare the data for the selected project by performing any necessary preprocessing.
    """
    project_data = data[project_name]
    
    # Ensure the 'time', 'lat', and 'lon' columns are present in the data
    required_columns = ['time', 'lat', 'lon']
    if not all(col in project_data.columns for col in required_columns):
        raise ValueError(f"Missing required columns: {required_columns}")
    
    # Convert 'time' column to datetime (if needed)
    project_data['time'] = pd.to_datetime(project_data['time'], unit='s')
    
    return project_data
