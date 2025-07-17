# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
# )
# from PyQt5.QtCore import Qt
# import sys


# class LoginUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Pedal Power Login")
#         self.setFixedSize(350, 250)
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()
#         layout.setAlignment(Qt.AlignCenter)

#         # Title
#         title = QLabel("Pedal Power Login")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 18px; font-weight: bold;")
#         layout.addWidget(title)
#         layout.addSpacing(20)

#         # Username
#         username_label = QLabel("Username:")
#         username_label.setStyleSheet("font-size: 13px;")
#         layout.addWidget(username_label)
#         username_entry = QLineEdit()
#         username_entry.setDisabled(True)
#         layout.addWidget(username_entry)

#         # Password
#         password_label = QLabel("Password:")
#         password_label.setStyleSheet("font-size: 13px;")
#         layout.addWidget(password_label)
#         password_entry = QLineEdit()
#         password_entry.setEchoMode(QLineEdit.Password)
#         password_entry.setDisabled(True)
#         layout.addWidget(password_entry)

#         layout.addSpacing(10)

#         # Login Button
#         login_button = QPushButton("Login")
#         login_button.setFixedWidth(150)
#         login_button.setStyleSheet("font-size: 13px;")
#         login_button.setEnabled(True)
#         layout.addWidget(login_button, alignment=Qt.AlignCenter)

#         # Add stretch to center everything
#         layout.addStretch()

#         self.setLayout(layout)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LoginUI()
#     window.show()
#     sys.exit(app.exec_())
