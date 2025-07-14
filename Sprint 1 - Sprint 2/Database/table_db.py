import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect("pedalpower.db")

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# -------------------------------
# 🧍 USERS TABLE (all fields required)
# -------------------------------
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
)
''')

# -------------------------------
# 🛡️ ADMINS TABLE
# -------------------------------
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Admins (
    AdminID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
)
''')

# -------------------------------
# 🚴 BIKING RECORDS TABLE
# -------------------------------
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS BikeRecords (
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    DistanceKM REAL NOT NULL,
    RecordDate TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)
''')

# -------------------------------
# 🛠️ INSERT DEFAULT ADMIN IF NOT EXISTS (plain password)
# -------------------------------
cursor.execute("SELECT * FROM Admins WHERE Username = 'admin'")
if not cursor.fetchone():
    cursor.execute(
        "INSERT INTO Admins (Username, Password) VALUES (?, ?)",
        ('admin', 'admin123')  # Store plain text password directly
    )
    print("✅ Default admin account 'admin' created.")

# -------------------------------
# 🛠️ INSERT DEFAULT USER IF NOT EXISTS (plain password)
# -------------------------------
cursor.execute("SELECT * FROM Users WHERE Username = 'user'")  # Correct table name
if not cursor.fetchone():
    cursor.execute(
        "INSERT INTO Users (Username, Password) VALUES (?, ?)",
        ('user', 'user123')  # Store plain text password directly
    )
    print("✅ Default user account 'user' created.")

# ✅ Finalize
conn.commit()
conn.close()

print("✅ Database setup complete — pedalpower.db is ready.")
