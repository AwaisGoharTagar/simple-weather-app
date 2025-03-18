import streamlit as st
import requests


API_KEY = "b1b15e88fa797225412429c1c50c122a1"

# Function to get weather data
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("🌤 Simple Weather App")

city = st.text_input("Enter city name:", "")

if st.button("Get Weather"):
    if city:
        data = get_weather(city)
        if data:
            st.success(f"Weather in {city}")
            st.write(f"🌡 *Temperature:* {data['main']['temp']}°C")
            st.write(f"☁ *Condition:* {data['weather'][0]['description'].capitalize()}")
            st.write(f"💨 *Wind Speed:* {data['wind']['speed']} m/s")
            st.write(f"🌍 *Country:* {data['sys']['country']}")
        else:
            st.error("City not found! Please try again.")
    else:
        st.warning("Please enter a city name.")

