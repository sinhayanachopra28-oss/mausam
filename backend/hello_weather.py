# hello_weather.py - Mausam's first backend script
# Gets live weather for Chandigarh and prints it, Gen Z style.

import requests  # the "waiter" that talks to APIs

# 1. Where is Chandigarh? (latitude, longitude)
LAT, LON = 30.7333, 76.7794

# 2. The API address (Open-Meteo is free, no key needed)
URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LAT,
    "longitude": LON,
    "current": "temperature_2m,apparent_temperature,relative_humidity_2m,precipitation,wind_speed_10m",
    "timezone": "Asia/Kolkata",
}

# 3. Place the order and wait for the food
response = requests.get(URL, params=params, timeout=10)
response.raise_for_status()          # stop with an error if something went wrong
data = response.json()["current"]    # turn the JSON reply into a Python dictionary

temp = data["temperature_2m"]
feels = data["apparent_temperature"]
humidity = data["relative_humidity_2m"]
rain = data["precipitation"]
wind = data["wind_speed_10m"]

# 4. Mau's vibe check
if rain > 0:
    vibe = "rain era unlocked, grab that umbrella"
elif temp >= 35:
    vibe = "it's giving oven, stay hydrated"
elif temp <= 12:
    vibe = "hoodie szn, bestie"
else:
    vibe = "main character weather, go outside"

# 5. Print the report
print("Mausam | Chandigarh, right now")
print(f"Temperature : {temp}°C (feels like {feels}°C)")
print(f"Humidity    : {humidity}%")
print(f"Rain        : {rain} mm")
print(f"Wind        : {wind} km/h")
print(f"Mau says    : {vibe}")