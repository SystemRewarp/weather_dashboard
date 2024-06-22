import streamlit as st
import requests
import pandas as pd
import numpy as np
# st.video('https://www.youtube.com/watch?v=-nc146I26SU')
# st.sidebar.write('Sadev')
# st.subheader('Adelaide')
# st.button("Reset")
# if st.button("Print Name"):
#  st.write("Sadev Wijesuriya")
# else:
#  st.write("")
#st.video('https://www.youtube.com/watch?v=DSIZ0iLS310')


# Reply = requests.get('https://api.open-meteo.com/v1/forecast?latitude=-34.9287&longitude=138.5986&daily=temperature_2m_max,wind_speed_10m_max&timezone=Australia%2FSydney&past_days=14&forecast_days=1')
# Total = Reply.json()
# Past_Max_Temp = Total['daily']['temperature_2m_max']
# df_PMT = pd.DataFrame(Past_Max_Temp,)
# st.write('Line Chart For Maximum Temperature In The Past 15 Days:')
# st.line_chart(df_PMT)
# Past_Max_Wind_Speed = Total['daily']['wind_speed_10m_max']
# df_PMWS =pd.DataFrame(Past_Max_Wind_Speed)
# st.write('Line Chart For Maximum Wind Speed In The Past 15 Days:')
# st.line_chart(df_PMWS)


st.title('Weather Dashboard')
st.subheader('Australia/Adelaide')


answer_Day_Night = requests.get ('https://api.open-meteo.com/v1/forecast?latitude=-34.9287&longitude=138.5986&current=is_day&timezone=auto')
Value4 = answer_Day_Night.json()
Day_Night = Value4['current']['is_day']


answer_Current = requests.get ('https://api.open-meteo.com/v1/forecast?latitude=-34.9287&longitude=138.5986&current=temperature_2m,wind_speed_10m')
Value2 = answer_Current.json()
Temp = Value2['current']['temperature_2m']
Wind_Speed = Value2['current']['wind_speed_10m']

st.image(f"https://flagcdn.com/80x60/{'au'}.png")

col1, col2, col3 = st.columns(3)
col1.metric('Current Temperature (˚C)', Temp)
col2.metric("Current Wind Speed (km/h)", Wind_Speed)
if Day_Night == 0:
   col3.metric('Day/Night', 'Night')
else:
   col3.metric('Day/Night', 'Day')


response = requests.get ('https://api.open-meteo.com/v1/forecast?latitude=-34.9287&longitude=138.5986&current=temperature_2m,is_day,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,uv_index_max&timezone=Australia%2FSydney')
Value1 = response.json()
Lat = Value1['latitude']
Long = Value1['longitude']
st.sidebar.write('Latitude', Lat)
st.sidebar.write('Longitude', Long)


st.sidebar.write('Current Temperature In Adelaide', Temp )
st.sidebar.write('Current Wind Speed In Adelaide', Wind_Speed )

answer_Daily_Maxes = requests.get('https://api.open-meteo.com/v1/forecast?latitude=-34.9287&longitude=138.5986&daily=temperature_2m_max,wind_speed_10m_max&timezone=auto')
Value3 = answer_Daily_Maxes.json()
Daily_Max_Temp = Value3['daily']['temperature_2m_max']
Daily_Max_Wind_Speed = Value3['daily']['wind_speed_10m_max']






option = st.sidebar.selectbox( 
 'Choose Data To Predict',
['Daily Max Temperature', 'Daily Max Wind Speed'],
index=None,
placeholder="Select Weather Data To Show...",
)


if option == ('Daily Max Temperature'):
 df_DMT = pd.DataFrame(Daily_Max_Temp)
 st.line_chart(df_DMT)
elif option == ('Daily Max Wind Speed'):
  df_DMWS = pd.DataFrame(Daily_Max_Wind_Speed)
  st.line_chart(df_DMWS)
  
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://t4.ftcdn.net/jpg/00/84/05/99/360_F_84059942_SM8wo2KfPnKFjGo6E3Phcd4bNI9tYwmr.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()










