import sqlite3
from places_connector import get_attractions
from user_input import get_user_input

def plan_attractions(destination):
    attractions = get_attractions(destination)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()

    for activity in attractions:
        cursor.execute( "INSERT INTO itineraries (trip_id, activity, category) VALUES (?,?,?)", (1, activity, "attraction"))
    conn.commit()
    conn.close()
    print(f"Saved {len(attractions)} attractions for {destination}.")


def plan_itinerary(destination, start_date, end_date):
    from weather_api import get_weather_forecast
    weather = get_weather_forecast(destination, start_date, end_date)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trips (user_id, destination, weather, start_date, end_date) VALUES (?,?,?,?,?)", (1, destination, str(weather), start_date, end_date))
    conn.commit()
    conn.close()

    print(f"Saved weather for {destination}.")



# for testing purposes only remove for production because we will only make the intinerary, and it will include the attractions and the weather

print("welcome to tagalong!")
destination, start_date, end_date = get_user_input()
plan_attractions(destination)
plan_itinerary(destination, start_date, end_date)

