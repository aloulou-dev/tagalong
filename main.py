import sqlite3
from places_connector import get_attractions

def plan_attractions():
    from user_input import get_user_input
    destination, start_date, end_date = get_user_input()
    attractions = get_attractions(destination)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()

    for activity in attractions:
        cursor.execute( "INSERT INTO itineraries (trip_id, activity, category) VALUES (?,?,?)", (1, activity, "attraction"))
    conn.commit()
    conn.close()
    print(f"Saved {len(attractions)} attractions for {destination}.")


def plan_itinerary():
    from user_input import get_user_input
    from weather_api import get_weather_forecast
    destination, start_date, end_date = get_user_input()
    weather = get_weather_forecast(destination, start_date, end_date)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trips (user_id, destination, weather, start_date, end_date) VALUES (?,?,?,?,?)", (1, destination, str(weather), start_date, end_date))
    conn.commit()
    conn.close()

    print(f"Saved weather for {destination}.")



# for testing purposes only remove for production because we will only make the intinerary, and it will include the attractions and the weather

print("welcome to tagalong!")
choice = input("Type 1 to plan attractions, 2 to plan itinerary, or 3 to do both:")
if choice == "1":
    plan_attractions()
elif choice == "2":
    plan_itinerary()
elif choice == "3":
    plan_attractions()
    plan_itinerary()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
        
