""" Adding on top of Eva's code """
import sqlite3

conn = sqlite3.connect("tagalong.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL 
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS trips(
    trip_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    destination TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS itineraries(
    itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER NOT NULL,
    activity TEXT NOT NULL,
    category TEXT NOT NULL,
    date_time TEXT,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id)

);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS connections(
    connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    connected_user_id INTEGER NOT NULL,
    destination TEXT NOT NULL,
    date_time TEXT,
    start_end TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (connected_user_id) REFERENCES users(user_id)
);
""")

conn.commit()
conn.close()
print("tables created")