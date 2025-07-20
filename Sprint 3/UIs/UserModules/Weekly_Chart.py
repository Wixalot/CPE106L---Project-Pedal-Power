from PyQt5.QtWidgets import QGroupBox, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def Weekly_Chart_Group(self, username):

    # Store the username for display and functionality
    self.username = username

    # Creating a group box for Weekly Chart
    Weekly_Chart_Group = QGroupBox("", self)
    Weekly_Chart_Group.setGeometry(50, 110, 420, 380)
    Weekly_Chart_Group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: transparent;
            }
        """)

    # Widget for Weekly Chart
    label = QLabel("Weekly Biking Progress\n(km)", Weekly_Chart_Group)
    label.setGeometry(120, 20, 185, 40)
    label.setFont(QFont("Arial", 12, QFont.Bold))
    label.setAlignment(Qt.AlignCenter)

    # Chart for Weekly Chart Calculation

    # Weekly data
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    values = [0, 0, 0, 0, 0, 0, 0]  # Default values

    # Getting the values from the log file
    file_path = "Database/Users_log_Data.txt"
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
                    for i in range(len(file_values)):
                        values[i] = file_values[i]
                    break

    except Exception as e:
        QMessageBox.warning(self, "Error", f"Failed to load weekly data: {e}")
    except FileNotFoundError:
        QMessageBox.warning(self, "Error", "Weekly data file not found.")

    # Display the Weekly Chart
    import matplotlib.pyplot as plt

    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(4, 2.5), dpi=100)
    ax.plot(days, values, marker='o', color='blue')
    ax.set_title('Weekly Biking Progress')
    ax.set_xlabel('Day')
    ax.set_ylabel('Distance (km)')
    ax.yaxis.grid(True)

    # Embed chart in PyQt
    canvas = FigureCanvas(fig)
    canvas.setParent(Weekly_Chart_Group)
    canvas.setGeometry(30, 100, 360, 220)
    canvas.setStyleSheet("""
            FigureCanvas {
                background-color: transparent;
            }
        """)
    canvas.show()
