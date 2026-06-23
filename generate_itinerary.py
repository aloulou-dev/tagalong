from user_input import get_user_input
from weather_api import get_weather_forecast

destination, start_date, end_date = get_user_input()

weather = get_weather_forecast(destination, start_date, end_date)
for day in weather:
    print(day)

#later genAI can use weather