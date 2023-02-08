import streamlit as st
import pandas as pd

st.title("Calgary Fire Station Response Lag Time Analysis")

# Load data into a pandas dataframe
data = pd.read_csv("fire_station_data.csv")

# Filter data for FSA level
selected_level = st.selectbox("Select FSA Level", options=data['FSA'].unique())
filtered_data = data[data['FSA'] == selected_level]

# Plot histogram of response lag times
st.write("Response Lag Time (in minutes)")
st.bar_chart(filtered_data['Response Lag Time'])

# Show statistics on response lag times
st.write("Mean Response Lag Time:", filtered_data['Response Lag Time'].mean())
st.write("Median Response Lag Time:", filtered_data['Response Lag Time'].median())
st.write("Standard Deviation of Response Lag Time:", filtered_data['Response Lag Time'].std())

# Show a table of top 5 Fire Stations with highest mean response lag times
st.write("Top 5 Fire Stations with highest mean response lag times:")
st.write(filtered_data.groupby("Fire Station Name").mean().sort_values(by='Response Lag Time', ascending=False).head(5))
