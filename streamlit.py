import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
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

# df = df.set_index('date')

# df

# st.line_chart(df)

# st.subheader('I love avocados.')


# df = pd.read_csv("avovol.csv")

# # st.write(df)
# st.title("Avocado Price x Volume Purchased")
# st.area_chart(df)



# st.title("Avocado Prices in 2017")
# df2 = pd.read_csv("avocado.csv")
# df2['Date'] =  df2['Date'].astype('datetime64[ns]')
# fig = px.line(df, x="Date", y="Average Price")


# st.plotly_chart(fig)


# df.columns[0]].as_matrix()
# list2 = matrix2.tolist()

# temp = {
#   "2000-01-01": 100,
#   "2000-01-02": 150
# }

# df = pd.DataFrame.from_dict(temp, index=[0])
# df = pd.DataFrame.from_records([{ '2000-01-01':1,'2000-01-02':2 }])

# df = pd.DataFrame(temp, columns=['a'])


# st.line_chart(df)


# st.area_chart(df.columns[0], df.columns[1])


# df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

# st.vega_lite_chart(df, {
#     'mark': 'circle',
#     'encoding': {
#     'x': {'field': 'a', 'type': 'quantitative'},
#     'size': {'field': 'c', 'type': 'quantitative'},
#     'color': {'field': 'c', 'type': 'quantitative'},
#     },
# })


# st.title("Guac is extra.")



# st.title("World Happiness")
# st.text('Data from https://www.kaggle.com/mathurinache/world-happiness-report-20152021')

# df = pd.read_csv("Happiness.csv")
# st.write(df)

# united_states = st.checkbox('United States')
# canada = st.checkbox('Canada')
# finland = st.checkbox('Finland')
# denmark = st.checkbox('Denmark')




# if united_states:


# st.text('Data from https://www.kaggle.com/mathurinache/world-happiness-report-20152021')

# df = pd.read_csv("Happiness.csv")
# st.write(df)

# united_states = st.checkbox('United States')
# canada = st.checkbox('Canada')
# finland = st.checkbox('Finland')
# denmark = st.checkbox('Denmark')




# if US:
#     st.write('Great!')


# #chart_data = pd.DataFrame(df)
# st.bar_chart(df)

# # st.write(pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column': [10, 20, 30, 40]
# # }))


# st.pydeck_chart(pdk.Deck(
#      map_style='mapbox://styles/mapbox/light-v9',
#      initial_view_state=pdk.ViewState(
#          latitude=37.76,
#          longitude=-122.4,
#          zoom=11,
#          pitch=50,
#      ),
#      layers=[
#          pdk.Layer(
#             'HexagonLayer',
#             data=df,
#             get_position='[lon, lat]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#          ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=df,
#              get_position='[lon, lat]',
#              get_color='[200, 30, 0, 160]',
#              get_radius=200,
#          ),
#      ],
#  ))
