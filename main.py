import sqlite3
from places_connector import get_attractions
from user_input import get_user_input
from ai_itinerary import generate_ai_itinerary
from database import get_or_create_user

def plan_attractions(destination):
    attractions = get_attractions(destination)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()

    for activity in attractions:
        cursor.execute( "INSERT INTO itineraries (trip_id, activity, category) VALUES (?,?,?)", (1, activity, "attraction"))
    conn.commit()
    conn.close()
    print(f"Saved {len(attractions)} attractions for {destination}.")
    return attractions


def plan_itinerary(user_id, destination, start_date, end_date):
    from weather_api import get_weather_forecast
    weather = get_weather_forecast(destination, start_date, end_date)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trips (user_id, destination, start_date, end_date) VALUES (?,?,?,?)", (user_id, destination, start_date, end_date))
    conn.commit()
    conn.close()

    print(f"Saved weather for {destination}.")
    return weather



# for testing purposes only remove for production because we will only make the intinerary, and it will include the attractions and the weather

print("welcome to tagalong!")
user_name, user_email, destination, start_date, end_date = get_user_input()
user_id = get_or_create_user(user_name, user_email)
attractions = plan_attractions(destination)
weather = plan_itinerary(user_id, destination, start_date, end_date)

itinerary = generate_ai_itinerary(destination, attractions, weather)
print("\n--- Your Tagalong Itinerary ---")
print(itinerary)

