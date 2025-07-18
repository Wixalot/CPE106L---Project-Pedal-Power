import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from UIs.LoginWINDOW import LoginWindow
from UIs.view_ui import ViewWindow

DB_PATH = 'Database/pedalpower.db'
ICON_PATH = 'Assets/eye.png'

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/admin_ui.ui', self)
        self.setWindowTitle('Pedal Power Admin')
        self.setup_ui()
        self.load_users()

    def setup_ui(self):
        self.btnAdd.clicked.connect(self.add_user)
        self.btnUpdate.clicked.connect(self.update_user)
        self.btnDelete.clicked.connect(self.delete_user)
        self.btnView.clicked.connect(self.open_view_window)
        self.btnRefresh.clicked.connect(self.refresh_from_button)
        self.btnLogout.clicked.connect(self.logout)

        self.tableUsers.itemSelectionChanged.connect(self.toggle_buttons)
        self.toggle_buttons()

    def load_users(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT UserID, Username, Password FROM Users")
            users = cursor.fetchall()
            conn.close()

            self.tableUsers.setRowCount(0)  # Clear previous content

            if not users:
                return  # Show blank table if no users

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
            QMessageBox.critical(self, "Database Error", str(e))

    def toggle_buttons(self):
        has_selection = bool(self.tableUsers.selectedItems())
        self.btnUpdate.setEnabled(has_selection)
        self.btnDelete.setEnabled(has_selection)
        self.btnView.setEnabled(has_selection)

    def toggle_password(self, row):
        item = self.tableUsers.item(row, 2)
        current = item.text()
        actual = item.data(Qt.UserRole)
        item.setText(actual if current == "••••••••" else "••••••••")

    def add_user(self):
        username = self.UsernameTextbox.toPlainText().strip()
        password = self.PasswordTextbox.toPlainText().strip()

        if not (username and password):
            QMessageBox.warning(self, "Input Error", "Username and Password are required.")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)",
                           (username, password))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", f"User '{username}' added successfully.")
            self.refresh_from_button()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "Username already exists.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_user(self):
        selected = self.tableUsers.selectedItems()
        if not selected:
            return

        selected_row = self.tableUsers.currentRow()
        user_id_item = self.tableUsers.item(selected_row, 0)
        if not user_id_item:
            return

        try:
            user_id = int(user_id_item.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid User ID.")
            return

        confirm = QMessageBox.question(self, "Confirm Delete",
                                       f"Delete user ID {user_id} and all their biking records?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM BikeRecords WHERE UserID = ?", (user_id,))
            cursor.execute("DELETE FROM Users WHERE UserID = ?", (user_id,))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Deleted", f"User {user_id} deleted.")
            self.refresh_from_button()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def update_user(self):
        selected = self.tableUsers.selectedItems()
        if not selected:
            return

        selected_row = self.tableUsers.currentRow()
        user_id_item = self.tableUsers.item(selected_row, 0)
        if not user_id_item:
            return

        try:
            user_id = int(user_id_item.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid User ID.")
            return

        username = self.UsernameTextbox.toPlainText().strip()
        password = self.PasswordTextbox.toPlainText().strip()

        if not (username and password):
            QMessageBox.warning(self, "Input Error", "Username and Password are required.")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET Username = ?, Password = ? WHERE UserID = ?",
                           (username, password, user_id))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Updated", f"User ID {user_id} updated.")
            self.refresh_from_button()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def open_view_window(self):
        selected_row = self.tableUsers.currentRow()
        if selected_row >= 0:
            user_id_item = self.tableUsers.item(selected_row, 0)  # Column 0 = UserID
            if user_id_item:
                try:
                    user_id = int(user_id_item.text())
                    self.view_window = ViewWindow(user_id)
                    self.view_window.show()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Invalid User ID format.")

    def refresh_from_button(self):
        self.UsernameTextbox.clear()
        self.PasswordTextbox.clear()
        self.load_users()

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
