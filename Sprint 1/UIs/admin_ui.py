import sys
import os
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

DB_PATH = 'Database/pedalpower.db'
ICON_PATH = os.path.join(os.path.dirname(__file__), "Assets", "eye.png")

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('admin_ui.ui', self)
        self.setWindowTitle('Pedal Power Admin')

        # Initial setup
        self.load_users()
        self.setup_ui()

    def setup_ui(self):
        # Disable buttons until a user is selected
        self.btnUpdate.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnView.setEnabled(False)

        # For now, connect buttons to print statements
        self.btnAdd.clicked.connect(lambda: print("Add clicked"))
        self.btnUpdate.clicked.connect(lambda: print("Update clicked"))
        self.btnDelete.clicked.connect(lambda: print("Delete clicked"))
        self.btnView.clicked.connect(lambda: print("View clicked"))
        self.btnRefresh.clicked.connect(lambda: print("Refresh clicked"))

        # Refresh user list when clicked (for next sprint)
        #self.btnRefresh.clicked.connect(self.load_users)

        # Toggle buttons when a row is selected
        self.tableUsers.itemSelectionChanged.connect(self.toggle_buttons)

        # 🔒 Logout button
        self.btnLogout.clicked.connect(self.logout)

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

            # Populate table
            self.tableUsers.setRowCount(len(users))
            self.tableUsers.setColumnCount(4)
            self.tableUsers.setHorizontalHeaderLabels(["User ID", "Username", "Password", "Show"])

            for row_idx, user in enumerate(users):
                for col_idx, value in enumerate(user):
                    display_text = "••••••••" if col_idx == 2 else str(value)
                    item = QTableWidgetItem(display_text)
                    item.setData(Qt.UserRole, value)  # Store actual password
                    self.tableUsers.setItem(row_idx, col_idx, item)

                # Add eye icon button to toggle password visibility
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

    def logout(self):
        print("Logging out...")
        self.close()
        # Future enhancement: return to LoginWindow here if needed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
