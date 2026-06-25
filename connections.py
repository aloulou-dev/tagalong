import sqlite3 

def connect_with_users(trip_id):
    conn = sqlite3.connect("tagalong.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT destination, start_date, end_date
        FROM trips
        WHERE trip_id = ?
        """,
        (trip_id,)
    )

    current_trip = cursor.fetchone()

    if current_trip is None:
        print("Trip not found")
        conn.close()
        return

    destination, start_date, end_date = current_trip

    cursor.execute(
        """
        SELECT users.name, users.email, trips.destination, trips.start_date, trips.end_date
        FROM trips
        JOIN users ON trips.user_id = users.user_id
        WHERE trips.destination = ?
        AND trips.trip_id != ?
        AND trips.start_date <= ?
        AND trips.end_date >= ?
        """,
        (destination, trip_id, end_date, start_date)
    )

    matches = cursor.fetchall()

    if matches:
        print("\nUsers with overlapping trips: ")
        for name, email, city, start, end in matches:
            print(f"- {name} ({email}) will be in {city} from {start} to {end}")
    else:
        print(f"\nNo users found with overlapping trips to {destination}.")

    conn.close()