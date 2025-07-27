from PyQt5.QtWidgets import QGroupBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


def Emissions_Save_Group(self, username):

    # Store the username for display and functionality

    # Creating a group box for Emissions Save
    emissions_group = QGroupBox("", self)
    emissions_group.setGeometry(490, 110, 230, 180)
    emissions_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: transparent;
            }
        """)

    # Widget for Emissions Save
    label = QLabel("Emissions Save", emissions_group)
    label.setGeometry(40, 30, 150, 15)
    label.setFont(QFont("Arial", 12, QFont.Bold))
    label.setAlignment(Qt.AlignCenter)

    # Logic for Emissions Save Calculation

    def Emissions_Save_Calculation(km):

        # Function to calculate emissions saved based on distance
        car_emissions = 108.2  # g/km
        emission_saved = (car_emissions * km) / 1000  # Convert to kg

        return emission_saved

    # File path for the database
    file_path = "Database/pedalpower.db"

    try:

        # Get the distance from the user in the database - Geoffrey Task

        # Get the distance from the user in the database - Geoffrey Task
        import sqlite3

        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()

        # Get the UserID of the given username
        cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            cursor.execute("SELECT SUM(DistanceKM) FROM BikeRecords WHERE UserID = ?", (user_id,))
            result = cursor.fetchone()
            km = result[0] if result[0] else 0
        else:
            km = 0

        conn.close()

        emissions_saved = Emissions_Save_Calculation(km)

        # Display the Emissions Saved
        Number_emissions = QLabel(
            f"{emissions_saved:.2f}", emissions_group)
        Number_emissions.setGeometry(30, 35, 90, 120)
        Number_emissions.setStyleSheet("""
                QLabel {
                    font-size: 60px;
                    font-family: DilleniaUPC;
                    color: black;
                }
            """)
        Number_emissions.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

    Emissions_label = QLabel("kg of \nCO2 saved", emissions_group)
    Emissions_label.setGeometry(130, 35, 90, 120)
    Emissions_label.setStyleSheet("""
            QLabel {
                font-size: 10px;
                font-family: Arial;
                color: black;
            }
        """)
    Emissions_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    # Add a method to refresh the emissions saved display
    def refresh_emissions():
        try:
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT UserID FROM Users WHERE Username = ?", (username,))
            user = cursor.fetchone()
            if user:
                user_id = user[0]
                cursor.execute(
                    "SELECT SUM(DistanceKM) FROM BikeRecords WHERE UserID = ?", (user_id,))
                result = cursor.fetchone()
                km = result[0] if result[0] else 0
            else:
                km = 0
            conn.close()
            emissions_saved = Emissions_Save_Calculation(km)
            Number_emissions.setText(f"{emissions_saved:.2f}")
        except Exception as e:
            print(f"An error occurred during refresh: {e}")

    # Expose the refresh function for external calls
    emissions_group.refresh_emissions = refresh_emissions
    self.refresh_emissions = refresh_emissions
