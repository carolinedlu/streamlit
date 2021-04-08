import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import altair as alt

from PIL import Image

st.title("👋🏼 Hi! I'm Caroline.")
st.subheader('I am a Solution Architect at Klaviyo.')
image = Image.open('CarolineLuHeadshot.jpg')
st.image(image, width=698)

st.subheader('Analysis of titles of posts in r/wallstreetbets from September 28th, 2020 to April 6, 2021.')
# df = pd.DataFrame([['gme',3368],['buy',2494],['robinhood',2453],['hold',1932]])

words = np.array(['gme','buy','robinhood','hold','amc','bb','nok'])
frequencies = np.array([3368,2494,2453,1932,1816,866,841])
chart_data = pd.DataFrame()
chart_data['Words'] = words
chart_data['Frequencies'] = frequencies

chart_v1 = alt.Chart(chart_data, height=500, width=500).mark_bar().encode(
x = 'Words',
y = 'Frequencies')
# st.bar_chart(chart_data['Words'],chart_data['Frequencies'])
st.write("","",chart_v1)

#    [3368, 2494, 2453, 1932],
#    columns=["gme", "buy", "robinhood", "hold"]
# )

# st.bar_chart(df)

# df = pd.DataFrame({
#   'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
#   'Avocado Price': [10, 20, 30, 40]
# })
