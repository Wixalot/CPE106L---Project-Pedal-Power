from PyQt5.QtWidgets import QGroupBox, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import re


def Km_Inputs(self, username):

    # Store the username for display and functionality
    self.username = username

    # Creating a group box for Km Inputs
    Km_Inputs_Group = QGroupBox("", self)
    Km_Inputs_Group.setGeometry(490, 310, 231, 180)
    Km_Inputs_Group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: transparent;
            }
        """)

    # Widget for Km Inputs
    label = QLabel("Fuel Your Progress", Km_Inputs_Group)
    label.setGeometry(40, 30, 150, 15)
    label.setFont(QFont("Arial", 12, QFont.Bold))
    label.setAlignment(Qt.AlignCenter)

    # Input Field for Km
    self.label_km = QLineEdit(Km_Inputs_Group)
    self.label_km.setGeometry(60, 110, 110, 40)
    self.label_km.setFont(QFont("Calibri Light", 10))
    self.label_km.setAlignment(Qt.AlignCenter)
    self.label_km.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                background: rgba(255, 255, 255);
                border-radius: 3px;
                font-size: 14px;
            }
        """)

    # Setting a validator for the input field to accept only integers
    self.label_km.setValidator(QtGui.QDoubleValidator())

    import os

    def Km_Inputs_Logic():
        import sqlite3
        import datetime
        import re
        from PyQt5.QtWidgets import QMessageBox

        try:
            from UIs.UserModules.Weekly_Chart import refresh_chart
        except ImportError:
            def refresh_chart(username):
                pass

        file_path = "Database/Users_log_Data.txt"
        db_path = "Database/pedalpower.db"
        username = self.username
        start_date = datetime.date(2025, 7, 12)
        input_value = self.label_km.text().strip()

        # Validate input: must be a non-negative number
        try:
            km = int(float(input_value))  # Always store as integer
            if km < 0:
                raise ValueError("Distance cannot be negative.")
        except ValueError:
            QMessageBox.warning(
                self, "Invalid Input", "Please enter a valid non-negative number for kilometers.")
            return

        # Read user log data and find the user's line
        user_found = False
        lines = []
        with open(file_path, "r") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            user = line.split(",")[0]
            if user == username:
                user_found = True
                # Updated regex to match negative numbers (specifically -1)
                match = re.search(r'\[([-0-9,\s]+)\]', line)
                if match:
                    values_str = match.group(1).replace(" ", "")
                    file_values = [int(x) for x in values_str.split(",")]
                else:
                    file_values = [-1, -1, -1, -1, -1, -1, -1]
                break
        if not user_found:
            QMessageBox.warning(self, "Error", "User not found in log data.")
            return

        # Get UserID from Users table
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT UserID FROM Users WHERE Username=?", (username,))
        user_id_result = cursor.fetchone()
        if not user_id_result:
            conn.close()
            QMessageBox.warning(
                self, "Error", "UserID not found for this username.")
            return
        user_id = user_id_result[0]

        # Count total entries from the database to determine the next date
        cursor.execute(
            "SELECT COUNT(*) FROM BikeRecords WHERE UserID = ?", (user_id,))
        total_entries = cursor.fetchone()[0]

        entry_date = (
            start_date + datetime.timedelta(days=total_entries)).strftime('%Y-%m-%d')

        # Write this entry immediately to the database
        try:
            cursor.execute(
                "UPDATE BikeRecords SET DistanceKM = DistanceKM + ? WHERE UserID = ? AND RecordDate = ?",
                (int(km), user_id, entry_date)
            )
            if cursor.rowcount == 0:
                cursor.execute(
                    "INSERT INTO BikeRecords (UserID, DistanceKM, RecordDate) VALUES (?, ?, ?)",
                    (user_id, int(km), entry_date)
                )
            conn.commit()
        except Exception as e:
            QMessageBox.warning(self, "Database Error",
                                f"Failed to update totals: {e}")
            conn.close()
            return

        # Determine current day index based on filled entries in the log

        # Find the first -1 in file_values to determine the current day index
        try:
            day_idx = file_values.index(-1)
        except ValueError:
            day_idx = None  # All days are filled

        # Update the value for the current day if there is an unfilled day
        if day_idx is not None:
            file_values[day_idx] = int(km)
            # Save updated log before any reset
            new_line = f"{username},[{','.join(str(x) for x in file_values)}]\n"
            lines[idx] = new_line
            with open(file_path, "w") as f:
                f.writelines(lines)

            # Refresh chart to reflect new data
            try:
                self.refresh_weekly_chart()
            except Exception:
                pass  # Ignore chart errors for now

            # Now reset the week if it's complete
            if file_values.count(-1) == 0:
                QMessageBox.information(
                    self, "Week Complete", "Congratulations! Your weekly data has been added to your total.")
                file_values = [-1, -1, -1, -1, -1, -1, -1]
                new_line = f"{username},[{','.join(str(x) for x in file_values)}]\n"
                lines[idx] = new_line
                with open(file_path, "w") as f:
                    f.writelines(lines)
                # Optionally refresh chart again after reset
                try:
                    self.refresh_weekly_chart()
                except Exception:
                    pass
        else:
            # If all days are filled, reset week and update log
            QMessageBox.information(
                self, "Week Complete", "Congratulations! Your weekly data has been added to your total.")
            file_values = [-1, -1, -1, -1, -1, -1, -1]
            new_line = f"{username},[{','.join(str(x) for x in file_values)}]\n"
            lines[idx] = new_line
            with open(file_path, "w") as f:
                f.writelines(lines)
            try:
                self.refresh_weekly_chart()
            except Exception:
                pass

        conn.close()
        self.label_km.clear()

        # Show success message only if a new entry was added (not during week reset)
        if day_idx is not None:
            QMessageBox.information(
                self, "Success", f"{entry_date} updated with {km} km.")

    # Connecting the returnPressed signal to the Km_Inputs_Logic function
    self.label_km.returnPressed.connect(Km_Inputs_Logic)
