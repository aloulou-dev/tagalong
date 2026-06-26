import sqlite3
from places_connector import get_attractions
from user_input import get_user_input
from ai_itinerary import generate_ai_itinerary
from database import get_or_create_user

def plan_attractions(trip_id, destination):
    attractions = get_attractions(destination)

    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()

    for activity in attractions:
        cursor.execute( "INSERT INTO itineraries (trip_id, activity, category) VALUES (?,?,?)", (trip_id, activity, "attraction"))
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
    trip_id = cursor.lastrowid
    conn.commit()
    conn.close()

    print(f"Saved weather for {destination}.")
    return weather, trip_id


def modify_trip(trip_id):
    from connections import connect_with_users
    conn=sqlite3.connect("tagalong.db")
    cursor=conn.cursor()

    while True:
        choice = input(
            "\nWould you like to change anything?\n"
            "1) Change start date\n"
            "2) Change end date\n"
            "3) Change location\n"
            "4) Connect with other users during your trip\n"
            "5) Save changes and continue\n"
            "Choose an option: "
        )

        if choice == "1":
            new_start_date = input("Enter new start date (YYYY-MM-DD): ")
            cursor.execute("UPDATE trips SET start_date = ? WHERE trip_id = ?", (new_start_date, trip_id))
            conn.commit()
            print("Start date updated.")
        elif choice == "2":
            new_end_date = input("Enter new end date (YYYY-MM-DD): ")
            cursor.execute("UPDATE trips SET end_date = ? WHERE trip_id = ?", (new_end_date, trip_id))
            conn.commit()
            print("End date updated.")
        elif choice == "3":
            new_destination = input("Enter new destination: ")
            cursor.execute("UPDATE trips SET destination = ? WHERE trip_id = ?", (new_destination, trip_id))
            conn.commit()
            print("Location updated.")
        elif choice == "4":
            connect_with_users(trip_id)
        elif choice == "5":
            print("Changes saved. Enjoy your trip!")
            break
        else:
            print("Invalid choice. Please try again.")
    conn.close()


# for testing purposes only remove for production because we will only make the intinerary, and it will include the attractions and the weather

print("welcome to tagalong!")
user_name, user_email, destination, start_date, end_date = get_user_input()
user_id = get_or_create_user(user_name, user_email)
weather, trip_id = plan_itinerary(user_id, destination, start_date, end_date)
attractions = plan_attractions(trip_id, destination)

print("\nGenerating your itinerary... please wait")
itinerary = generate_ai_itinerary(destination, attractions, weather)
print("Done!\n")
print("--- Your Tagalong Itinerary ---")
print(itinerary)
modify_trip(trip_id)

