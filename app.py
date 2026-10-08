import streamlit as st
import requests
import time

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦️",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🌦️ Weather Dashboard")
st.caption("Real-time weather information 🌍")

# -----------------------------------
# SEARCH
# -----------------------------------

city = st.text_input(
    "🔎 Search for a city",
    placeholder="Example: Manila"
)

# -----------------------------------
# WEATHER APP
# -----------------------------------

if city:

    with st.spinner("🌍 Checking the weather..."):

        try:

            # -----------------------------------
            # GET CITY COORDINATES
            # -----------------------------------

            geo_response = requests.get(
                f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
            )

            geo_data = geo_response.json()

            if "results" not in geo_data:
                st.error("❌ City not found!")
                st.stop()

            location = geo_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            city_name = location["name"]
            country = location.get("country", "")

            # -----------------------------------
            # GET WEATHER
            # -----------------------------------

            weather_response = requests.get(
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={latitude}"
                f"&longitude={longitude}"
                f"&current=temperature_2m,"
                f"relative_humidity_2m,"
                f"wind_speed_10m,"
                f"weather_code"
            )

            weather_data = weather_response.json()

            current = weather_data["current"]

            # -----------------------------------
            # EXTRACT DATA
            # -----------------------------------

            temperature = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            wind_speed = current["wind_speed_10m"]
            weather_code = current["weather_code"]

            # -----------------------------------
            # WEATHER CONDITIONS
            # -----------------------------------

            if weather_code == 0:

                condition = "Clear Sky"
                emoji = "☀️"
                effect = "☀️ ☀️ ☀️"

            elif weather_code in [1, 2, 3]:

                condition = "Cloudy"
                emoji = "☁️"
                effect = "☁️ ☁️ ☁️"

            elif weather_code in [45, 48]:

                condition = "Foggy"
                emoji = "🌫️"
                effect = "🌫️ 🌫️ 🌫️"

            elif weather_code in [51, 53, 55, 56, 57]:

                condition = "Drizzle"
                emoji = "🌦️"
                effect = "💧 💧 💧"

            elif weather_code in [61, 63, 65, 66, 67]:

                condition = "Rain"
                emoji = "🌧️"
                effect = "💧 💧 💧 💧 💧"

            elif weather_code in [71, 73, 75, 77]:

                condition = "Snow"
                emoji = "❄️"
                effect = "❄️ ❄️ ❄️ ❄️"

            elif weather_code in [80, 81, 82]:

                condition = "Rain Showers"
                emoji = "🌧️"
                effect = "💧 💧 💧 💧"

            elif weather_code in [95, 96, 99]:

                condition = "Thunderstorm"
                emoji = "⛈️"
                effect = "⚡ 🌧️ ⚡"

            else:

                condition = "Unknown"
                emoji = "🌍"
                effect = "🌍"

            # -----------------------------------
            # WEATHER DISPLAY
            # -----------------------------------

            st.divider()

            st.subheader(f"📍 {city_name}, {country}")

            # Weather animation/effect
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:35px;
                    padding:10px;
                    animation: float 2s infinite alternate;
                ">
                    {effect}
                </div>

                <style>
                @keyframes float {{
                    from {{
                        transform: translateY(0px);
                    }}
                    to {{
                        transform: translateY(-8px);
                    }}
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            # Main weather icon
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:90px;
                ">
                    {emoji}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Temperature
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:60px;
                    font-weight:bold;
                ">
                    {temperature}°C
                </div>
                """,
                unsafe_allow_html=True
            )

            # Condition
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:24px;
                    margin-bottom:20px;
                ">
                    {condition}
                </div>
                """,
                unsafe_allow_html=True
            )

            # -----------------------------------
            # WEATHER STATS
            # -----------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "💧 Humidity",
                    f"{humidity}%"
                )

            with col2:

                st.metric(
                    "💨 Wind Speed",
                    f"{wind_speed} km/h"
                )

            # -----------------------------------
            # LOCATION DETAILS
            # -----------------------------------

            with st.expander("📍 Location Details"):

                st.write("Latitude:", latitude)
                st.write("Longitude:", longitude)

            st.divider()

            st.caption("Powered by Open-Meteo 🌍")


        except requests.exceptions.RequestException:

            st.error(
                "⚠️ Couldn't connect to the weather service."
            )

        except Exception as error:

            st.error(
                "⚠️ Something went wrong."
            )

            st.write(error)