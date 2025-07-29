from PyQt5.QtWidgets import QGroupBox, QLabel, QMessageBox
import re
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


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
    values = [None] * 7  # Default values: None for missing data

    # Getting the values from the log file
    file_path = "Database/Users_log_Data.txt"
    try:
        with open(file_path, "r") as f:
            for line in f:
                user = line.split(",")[0]
                match = re.search(r'\[([0-9,\s-]+)\]', line)
                if match:
                    values_str = match.group(1).replace(" ", "")
                    file_values = [int(x) for x in values_str.split(",")]
                else:
                    file_values = [-1] * 7
                if user == self.username:
                    for i in range(len(file_values)):
                        # Display 0 for -1 (unfilled), keep actual value otherwise
                        values[i] = file_values[i] if file_values[i] != -1 else 0
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

    def refresh_chart():
        nonlocal ax, canvas
        # Read weekly data again
        new_values = [0] * 7
        try:
            with open(file_path, "r") as f:
                for line in f:
                    user = line.split(",")[0]
                    match = re.search(r'\[([0-9,\s-]+)\]', line)
                    if match:
                        values_str = match.group(1).replace(" ", "")
                        file_values = [int(x) for x in values_str.split(",")]
                    else:
                        file_values = [-1] * 7
                    if user == self.username:
                        for i in range(len(file_values)):
                            # Display 0 for -1 (unfilled), keep actual value otherwise
                            new_values[i] = file_values[i] if file_values[i] != -1 else 0
                        break
        except Exception as e:
            QMessageBox.warning(
                self, "Error", f"Failed to load weekly data: {e}")
            return

        # Update chart data
        ax.clear()
        ax.plot(days, new_values, marker='o', color='blue')
        ax.set_title('Weekly Biking Progress')
        ax.set_xlabel('Day')
        ax.set_ylabel('Distance (km)')
        ax.yaxis.grid(True)
        canvas.draw()

    # Expose the refresh_chart method for external calls
    self.refresh_weekly_chart = refresh_chart
