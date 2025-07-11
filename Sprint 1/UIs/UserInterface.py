import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QGroupBox, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize


class User_Interface_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pedal Power: User Interface")

        # Setting the fixed size: 800 - height, 600 - width
        self.setFixedSize(800, 600)

        # Calling the Title function
        self.Title()

    # Title function to create the title label and line
    def Title(self):
        # Creating a label
        label_Title = QLabel("Pedal Power", self)
        label_Title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        label_Title.setGeometry(30, 30, 240, 50)
        label_Title.setWindowTitle("Pedal Power")
        label_Title.setFont(QFont("Cooper Black", 25))

        # breaker
        self.line = QFrame(self)
        self.line.setGeometry(30, 80, 731, 16)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # Calling the Log Out function
        self.Log_Out()

    def Log_Out(self):
        # Log Out button
        LogOut = QPushButton("", self)
        LogOut.setGeometry(705, 40, 40, 40)
        LogOut.setIcon(QIcon("Assets/power-off.png"))
        LogOut.setIconSize(QSize(30, 30))
        LogOut.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border-radius: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 0.3);
            }
        """)

        def logout():

            # Log Out button functionality
            from LoginWINDOW import LoginWindow

            # Close the current window
            self.close()

            # Open the login window
            self.login_window = LoginWindow()
            self.login_window.show()

        # Connect the Log Out button to the logout function
        LogOut.clicked.connect(logout)


def execute():
    app = QApplication(sys.argv)
    window = User_Interface_Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    execute()
