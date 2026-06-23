import sqlite3

conn = sqlite3.connect("tagalong.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS itineraries(
    itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER NOT NULL,
    activity TEXT NOT NULL,
    category TEXT NOT NULL,
    date_time TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id)

);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS connections(
    connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    connected_user_id INTEGER NOT NULL,
    destination TEXT NOT NULL,
    date_time TEXT NOT NULL,
    start_end TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (connected_user_id) REFERENCES users(user_id)
);
""")

conn.commit()
conn.close()