import requests
from datetime import datetime

API_KEY = "ed71c3f5a1ec48d9b17190631262306"

def get_weather_forecast(destination, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    trip_length = (end - start).days + 1

    response = requests.get(
        "http://api.weatherapi.com/v1/forecast.json",
        params={
            "key": API_KEY,
            "q" : destination,
            "days": trip_length
        }
    )

    data = response.json()
    forecast_days = data["forecast"]["forecastday"]

    weather_summary =[]
    for day in forcast_days:
        weather_summary.append({
            "date" : day["date"],
            "condition" : day["day"]["condition"]["text"],
            "avg_temp_f" : day["day"]["avgtemp_f"],
            "max_temp_f" : day["day"]["maxtemp_f"],
            "min_temp_f" : day["day"]["mintemp_f"],
            "chance_of_rain" : day["day"]["daily_chance_of_rain"],
        })
    return weather_summary

