import streamlit as st
import requests

def get_weather(city):
    api_key = "your_weatherapi_key_here"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind = data['current']['wind_kph']

        return {
            "location": location,
            "temperature": temp,
            "condition": condition,
            "humidity": humidity,
            "wind": wind
        }
    else:
        return None

def main():
    st.title("My Weather App")
    st.header("Welcome to the dashboard")
    st.write("This is a simple weather app checking")

    city = st.text_input("Enter a city name", "")

    if city:
        weather = get_weather(city)
        if weather:
            st.subheader(f"Weather in {weather['location']}")
            st.write(f"Temperature: {weather['temperature']} °C")
            st.write(f"Condition: {weather['condition']}")
            st.write(f"Humidity: {weather['humidity']} %")
            st.write(f"Wind Speed: {weather['wind']} kph")
        else:
            st.error("Failed to retrieve weather data. Please check the city name or API key.")

if __name__ == "__main__":
    main()

