import streamlit as st
import pandas as pd
import json
from datetime import date
from urllib.request import urlopen
import time
import altair as alt
import folium
from streamlit_folium import st_folium
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("")
st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)#color: red;

# Load data into a pandas dataframe
data = pd.read_csv("fire_station_data.csv")
df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
#df_ems = pd.read_excel("EMS_Stations.xlsx")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# center on Liberty Bell, add marker
#m = folium.Map(tiles='OpenStreetMap',zoom_start=160)
m = shapefile.explore()
for idx, row in df_fire.iterrows():
    folium.Marker(location=[row["LAT"], row["LON"]], icon=folium.Icon(icon="circle", prefix='fa', color='blue')).add_to(m)#, row["LON"]], popup=row["Name"]
st_data = st_folium(m, width=500)
# shapefile.explore()

# #st.set_page_config(layout="wide")

# #Shapefile
# shapefile = gpd.read_file("clipped-to-calgary.shp",SHAPE_RESTORE_SHX = 'YES')
# shapefile.explore()
# shapefile.plot()
#Map
#st.map(df_ems)
st.map(df_fire)
# Filter data for FSA level
selected_level = st.selectbox("Select FSA Level", options=data['FSA'].unique())
filtered_data = data[data['FSA'] == selected_level]

# Plot histogram of response lag times
st.write("Response Lag Time (in minutes)")
st.bar_chart(filtered_data['Response Lag Time'])

# Show statistics on response lag times
col0, col1, m2,col2, m3, col3, col4= st.columns((1,1,1,1,1,1,1))
#m1.write('')
m2.write('')
m3.write('')
#m4.write('')
col0.write('')
col1.metric("Mean Response Lag Time:", f"{round(filtered_data['Response Lag Time'].mean(),2)} min")
col2.metric("Median Response Lag Time:", f"{round(filtered_data['Response Lag Time'].median(),2)} min")
col3.metric("Standard Deviation Response Lag Time:", f"{round(filtered_data['Response Lag Time'].std(),2)} min")
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
