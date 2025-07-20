from PyQt5.QtWidgets import QGroupBox, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


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


def Km_Inputs_Logic(self, km):

    # File path for the database
    file_path = "Database/pedalpower.db"

    try:
        with open(file_path, "r") as f:
            for line in f:

                # Splitting the line to get the username and values

                # User
                user = line.split(",")[0]

                # Values
                values_str = ",".join(line.split(
                    ",")[1:]).strip("\n").strip("[]")
                file_values = [int(x) for x in values_str.split(",")]

                # If the user matches the username, update the values
                if user == self.username:
                    break
    except FileNotFoundError:
        QMessageBox.warning(self, "Error", "Database file not found.")
    except Exception as e:
        QMessageBox.warning(self, "Error", f"An error occurred: {e}")
