""" Adding on top of Eva's code """
import sqlite3

conn = sqlite3.connect("tagalong.db")
cursor = conn.cursor()

def get_or_create_user(name, email):
    cursor.execute("SELECT user_id FROM users WHERE name = ? AND email = ?", (name, email))

    existing_user = cursor.fetchone()

    if existing_user:
        return existing_user[0]
    
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    return cursor.lastrowid


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL 
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS trips(
    trip_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
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

# Seed mock users and trips if database is empty
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    mock_users = [
        ("Alice Smith", "alice@example.com"),
        ("Bob Jones", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com")
    ]
    for name, email in mock_users:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

    mock_trips = [
        (1, "Paris", "2026-07-01", "2026-07-10"),
        (2, "Paris", "2026-07-05", "2026-07-15"),
        (3, "New York", "2026-07-01", "2026-07-08")
    ]
    for user_id, dest, start, end in mock_trips:
        cursor.execute(
            "INSERT INTO trips (user_id, destination, start_date, end_date) VALUES (?, ?, ?, ?)",
            (user_id, dest, start, end)
        )
    print("Mock users and trips seeded for the demo.")

conn.commit()
#conn.close()
#print("tables created")