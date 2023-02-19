import streamlit as st
import pandas as pd
import json
from datetime import date
from urllib.request import urlopen
import time
import altair as alt

st.set_page_config(layout="wide")
st.title("Calgary Fire Station Response Lag Time Analysis")
#st.set_page_config(layout="wide")

# Load data into a pandas dataframe
data = pd.read_csv("fire_station_data.csv")

#Map
#st.map(data)

# Filter data for FSA level
selected_level = st.selectbox("Select FSA Level", options=data['FSA'].unique())
filtered_data = data[data['FSA'] == selected_level]

# Plot histogram of response lag times
st.write("Response Lag Time (in minutes)")
st.bar_chart(filtered_data['Response Lag Time'])

# Show statistics on response lag times
m1,col0, col1, col2, col3, col4, m2= st.columns((1,1,1,1,1,1,1))
m1.write('')
m2.write('')
col0.write('')
col1.metric("Mean Response Lag Time:", round(filtered_data['Response Lag Time'].mean(),2)+"Minutes")
col2.metric("Median Response Lag Time:", round(filtered_data['Response Lag Time'].median(),2))
col3.metric("SD of Response Lag Time:", round(filtered_data['Response Lag Time'].std(),2))
col4.write('')


# Show a table of top 5 Fire Stations with highest mean response lag times
st.write("Top 5 Fire Stations with highest mean response lag times:")
st.write(filtered_data.groupby("Fire Station Name").mean().sort_values(by='Response Lag Time', ascending=False).head(5))

# Show a table of top 5 Fire Stations with least mean response lag times
st.write("Top 5 Fire Stations with least mean response lag times:")
st.write(filtered_data.groupby("Fire Station Name").mean().sort_values(by='Response Lag Time', ascending=True).head(5))

col1, col2 = st.columns(2)
col1.subheader("Response Lag Time (in minutes)")
col1.bar_chart(data,x='FSA' , y='Response Lag Time')#,  use_container_width=True
col2.subheader("Response Lag Time (in minutes)")
col2.bar_chart(data, x='FSA', y='Response Lag Time', use_container_width=False)
