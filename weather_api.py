import requests
from datetime import datetime
from user_input import get_user_input

API_KEY = "ed71c3f5a1ec48d9b17190631262306"

destination, start_date, end_date = get_user_input()
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

print("\n Trip Information")
print("------------------------")
print("Destination:", destination)
print("Start Date:", start_date)
print("End Date:", end_date)

print("\nWeather Information for", destination)
print("------------------------")
print("Destination:", data["location"]["name"])
print("Temperature:", data["current"]["temp_f"], "°F")
print("Condition:", data["current"]["condition"]["text"])