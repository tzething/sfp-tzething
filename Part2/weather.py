import streamlit as st
import requests


city = input("Enter a city name: ").strip()
url = f"https://wttr.in/{city}?format=3"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"\n Weather info: {response.text}")
    else:
        print("Could not fetch weather data.")
except Exception as e:
    print(" Error:", e)
