import sqlite3

DB_PATH = "Database/pedalpower.db"

def get_total_emissions_saved(username):
    """
    Returns the total emissions saved (in kg) for a given username.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get the UserID for the given username
        cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]

            # Get the total distance traveled by that user
            cursor.execute("SELECT SUM(DistanceKM) FROM BikeRecords WHERE UserID = ?", (user_id,))
            result = cursor.fetchone()
            total_km = result[0] if result[0] else 0
        else:
            total_km = 0

        conn.close()

        # Calculate emissions saved
        car_emissions = 108.2  # grams of CO₂ per km
        emissions_saved = (car_emissions * total_km) / 1000  # convert to kg
        return emissions_saved

    except Exception as e:
        print(f"❌ Error retrieving emissions saved: {e}")
        return 0.0
