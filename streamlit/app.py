import streamlit as st
import pandas as pd

# Title of the app
st.title("Simple Streamlit App")

# Create some dummy data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Emily Jones', 'Michael Brown'],
    'Age': [28, 34, 22, 45],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Teacher'],
    'Country': ['USA', 'Canada', 'UK', 'Australia']
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame as a table
st.table(df)

# Optionally, add some interaction
selected_name = st.selectbox("Select a Name", df['Name'])
st.write(f"You selected: {selected_name}")
