import requests
import pandas as pd
from datetime import datetime

CITIES = {
    "Johannesburg": {"lat": -26.2041, "lon": 28.0473},
    "Pretoria": {"lat": -25.7479, "lon": 28.2293},
    "Cape Town": {"lat": -33.9249, "lon": 18.4241},
    "Durban": {"lat": -29.8587, "lon": 31.0218},
}

def fetch_weather():
    results = []
    for city, coords in CITIES.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        response = requests.get(url, timeout=30)
        data = response.json()["current"]
        results.append({
            "city": city,
            "temperature_c": data["temperature_2m"],
            "humidity_percent": data["relative_humidity_2m"],
            "wind_speed_kmh": data["wind_speed_10m"],
            "fetched_at": datetime.utcnow().isoformat() + "Z"
        })
    return pd.DataFrame(results)