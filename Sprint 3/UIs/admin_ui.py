import sys
import os
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from LoginWINDOW import LoginWindow
from view_ui import ViewWindow  # Integrated ViewWindow import
from AdminModules.logout import logout
from AdminModules.admin_features import add_user, update_user, remove_user # Import admin features for button actions

DB_PATH = 'Database/pedalpower.db'
ICON_PATH = 'Assets/eye.png'

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/admin_ui.ui', self)
        self.setWindowTitle('Pedal Power Admin')

        self.load_users()
        self.setup_ui()

    def setup_ui(self):
        self.btnUpdate.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnView.setEnabled(False)

        self.btnAdd.clicked.connect(lambda: add_user(self))
        self.btnUpdate.clicked.connect(lambda: update_user(self))
        self.btnDelete.clicked.connect(lambda: remove_user(self))

        self.btnView.clicked.connect(self.open_view_window)  # Connected View button

        self.btnRefresh.clicked.connect(self.refresh_from_button) # Refresh button to reload users

        self.tableUsers.itemSelectionChanged.connect(self.toggle_buttons)
        self.btnLogout.clicked.connect(lambda: logout(self))  # Call logout from logout.py

    def toggle_buttons(self):
        has_selection = bool(self.tableUsers.selectedItems())
        self.btnUpdate.setEnabled(has_selection)
        self.btnDelete.setEnabled(has_selection)
        self.btnView.setEnabled(has_selection)

    def load_users(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT UserID, Username, Password FROM Users")
            users = cursor.fetchall()
            conn.close()

            self.tableUsers.setRowCount(len(users))
            self.tableUsers.setColumnCount(4)
            self.tableUsers.setHorizontalHeaderLabels(["User ID", "Username", "Password", "Show"])

            for row_idx, user in enumerate(users):
                for col_idx, value in enumerate(user):
                    display_text = "••••••••" if col_idx == 2 else str(value)
                    item = QTableWidgetItem(display_text)
                    item.setData(Qt.UserRole, value)
                    self.tableUsers.setItem(row_idx, col_idx, item)

                btnEye = QPushButton()
                btnEye.setIcon(QIcon(ICON_PATH))
                btnEye.setFlat(True)
                btnEye.clicked.connect(lambda _, r=row_idx: self.toggle_password(r))
                self.tableUsers.setCellWidget(row_idx, 3, btnEye)
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def toggle_password(self, row):
        item = self.tableUsers.item(row, 2)
        current = item.text()
        actual = item.data(Qt.UserRole)
        item.setText(actual if current == "••••••••" else "••••••••")

    def open_view_window(self):
        selected = self.tableUsers.selectedItems()
        if selected:
            user_id = int(selected[0].text())  # Pass selected user ID
            self.view_window = ViewWindow(user_id)
            self.view_window.show()

    def refresh_from_button(self):
        print("Refreshing user list...")
        self.load_users()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
