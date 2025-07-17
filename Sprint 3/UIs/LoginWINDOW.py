import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pedal Power: Login")

        # Setting the fixed size: 800 - height, 600 - width
        self.setFixedSize(800, 600)

        # calling the Login function
        self.Login()

    def Login(self):
        # Creating a label
        label_Title = QLabel("Pedal Power", self)
        label_Title.setAlignment(Qt.AlignCenter)
        label_Title.setGeometry(0, 0, self.width() - 25, self.height()-200)
        label_Title.setWindowTitle("Pedal Power")
        label_Title.setFont(QFont("Cooper Black", 40))

        # Username and Password input fields
        self.Username()
        self.Password()

        # Submit button
        self.Submit()

    def Username(self):
        # Creating a label for username
        label_username = QLabel("Username:", self)
        label_username.setAlignment(Qt.AlignCenter)

        # Declaration of x and y coordinates for the label
        self.usernameX = -135
        self.usernameY = 0

        label_username.setGeometry(
            self.usernameX, self.usernameY, self.width() + 25, self.height() - 50)
        label_username.setFont(QFont("Arial", 15))

        # Creating a line edit for username input
        self.username_input = QLineEdit(self)

        # Note: The setGeometry parameters are (x, y, width, height)
        self.username_input.setGeometry(
            self.width() // 2 - 65, self.height() // 2 - 40, 200, 30)

        self.username_input.setStyleSheet("""
            QLineEdit {
            border: 2px solid #ccc;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            font-size: 14px;
            font-family: Arial;
            }                             
        """)

    def Password(self):
        # Creating a label for password
        label_password = QLabel("Password:", self)

        label_password.setGeometry(
            self.width() // 2 - 175, self.height() // 2, 100, 30)
        label_password.setFont(QFont("Arial", 15))
        label_password.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Creating a line edit for password input
        self.password_input = QLineEdit(self)

        # Note: The setGeometry parameters are (x, y, width, height)
        self.password_input.setGeometry(
            self.width() // 2 - 65, self.height() // 2, 200, 30)

        self.password_input.setStyleSheet("""
            QLineEdit {
            border: 2px solid #ccc;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            font-size: 14px;
            font-family: Arial;
            }                             
        """)

        # Set initial echo mode to Password (hidden)
        self.password_input.setEchoMode(QLineEdit.Password)

        # A toggle button to check the visibility of the password
        toggle_button = QRadioButton("", self)
        toggle_button.setGeometry(
            self.width() // 2 + 140, self.height() // 2 + 5, 20, 20)

        # Condition to check the visibility of the password
        def toggle_password():
            if toggle_button.isChecked():
                self.password_input.setEchoMode(
                    QLineEdit.Normal)  # Show password
            else:
                self.password_input.setEchoMode(
                    QLineEdit.Password)  # Hide password

        toggle_button.toggled.connect(toggle_password)

    def Submit(self):

        # Creating a button for submitting the login form
        submit_button = QPushButton("Login", self)
        submit_button.setGeometry(
            self.width() // 2 - 65, self.height() // 2 + 45, 200, 30)
        submit_button.setFont(QFont("Arial", 15))
        submit_button.setStyleSheet("""
            QPushButton {
            background-color: #4CAF50;
            color: white;
            border: 1px solid #ADADAD;
            border-radius: 10px;
            padding: 5px 20px;
            font-size: 14px;
            }
            QPushButton:hover {
            background-color: #45a049;
            }
        """)

        # Function to handle the login action
        def handle_Login():
            username = self.username_input.text()
            password = self.password_input.text()

            # Path to the file containing the Database of both admin and user credentials
            file_path = "Database/pedalpower.db"

            # try block to read the file and compare for a successful login
            try:

                import sqlite3

                connection = sqlite3.connect(file_path)
                cursor = connection.cursor()

                # Checking if the username and password match in the admin table
                cursor.execute(
                    "SELECT * FROM Admins WHERE username=? AND password=?", (username, password))
                admin_result = cursor.fetchone()

                # Check user table
                cursor.execute(
                    "SELECT * FROM Users WHERE username=? AND password=?", (username, password))
                user_result = cursor.fetchone()

                if admin_result:

                    from UIs.admin_ui import AdminWindow as admin

                    # closing the login window before opening the next UI
                    self.close()

                    # Show the admin interface window
                    self.admin_window = admin()
                    self.admin_window.show()

                    # clear the input fields after successful login
                    self.username_input.clear()
                    self.password_input.clear()

                elif user_result:

                    from UIs.UserInterface import User_Interface_Window as UI

                    # closing the login window before opening the next UI
                    self.close()

                    # Show the main user interface window
                    self.ui_window = UI()
                    self.ui_window.show()

                    # Clear the input fields after successful login
                    self.username_input.clear()
                    self.password_input.clear()

                else:
                    print("Login failed. Please check your username and password.")

            except FileNotFoundError:
                print(f"Error: The file {file_path} does not exist.")

        # Connecting the submit button to the handle_Login function
        submit_button.clicked.connect(handle_Login)


def execute():

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    execute()
