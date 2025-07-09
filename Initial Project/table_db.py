import sqlite3

# ✅ Connect to SQLite DB (creates it if not exists)
conn = sqlite3.connect("pedalpower.db")

# ✅ Enable foreign key constraint enforcement
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# -------------------------------
# 🧍 USERS TABLE (all fields required)
# -------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
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
# 🛠️ INSERT DEFAULT ADMIN IF NOT EXISTS
# -------------------------------
cursor.execute("SELECT * FROM Admins WHERE Username = 'admin'")
if not cursor.fetchone():
    cursor.execute(
        "INSERT INTO Admins (Username, Password) VALUES (?, ?)",
        ('admin', 'admin123')
    )
    print("✅ Default admin account 'admin' created.")

# ✅ Finalize
conn.commit()
conn.close()

print("✅ Database setup complete — pedalpower.db is ready.")
