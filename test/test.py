import streamlit as st
from streamlit_folium import folium_static
import folium
import numpy as np

"# streamlit-folium"



locations = [[-26.205171,28.049815],[-33.925839,18.423218],[-26.190851,28.311338],
[-29.857896,31.029198],[-25.706944,28.229444],[-26.673133,27.926147],
[-33.917988,25.570066],[-22.945642,30.484972],[-26.258374,28.47173],
[-33.75757,25.397099],[-23.904485,29.468851],[-33.733781,18.975228],
[-26.852128,26.666719],[-33.963,22.461727],[-25.667562,27.242079],
[-28.732262,24.762315],[-32.847212,27.442179],[-25.775071,29.464821],
[-27.76952,30.791653],[-31.588926,28.784431],[-33.64651,19.448523],
[-26.716667,27.1],[-25.634731,27.780224],[-31.897563,26.875329],
[-25.85,25.633333],[-27.65036,27.234879],[-26.457937,29.465534],
[-33.304216,26.53276],[-28.230779,28.307071],[-33.592343,22.205482],
[-26.933655,29.241518],[-28.447758,21.256121],[-33.01167,17.944202],
[-23.833222,30.163506],[-34.036643,23.049704],[-32.25,24.55]]

from random import randint
durations = [randint(0, 10) for i in range(36)]

# center on Liberty Bell
m = folium.Map(location=[-26.205171,28.049815], zoom_start=5)

for point in range(0, len(locations)):
    folium.Marker(locations[point],popup="{}min".format(durations[point])).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)