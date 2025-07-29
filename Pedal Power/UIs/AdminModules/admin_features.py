# admin_features.py

import sqlite3
from PyQt5.QtWidgets import QMessageBox

DB_PATH = 'Database/pedalpower.db'

def remove_user(window):
    selected = window.tableUsers.selectedItems()
    if not selected:
        QMessageBox.warning(window, "No Selection", "Please select a user to remove.")
        return

    user_id = selected[0].text()
    confirm = QMessageBox.question(
        window,
        "Confirm Deletion",
        f"Are you sure you want to remove User ID {user_id}?",
        QMessageBox.Yes | QMessageBox.No
    )
    if confirm == QMessageBox.Yes:
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE UserID = ?", (user_id,))
            conn.commit()
            conn.close()
            QMessageBox.information(window, "Removed", f"User ID {user_id} has been removed.")
            window.load_users()
        except sqlite3.Error as e:
            QMessageBox.critical(window, "Database Error", str(e))

def add_user(window):
    user_id = window.UseridTextbox.toPlainText()
    username = window.UsernameTextbox.toPlainText()
    password = window.PasswordTextbox.toPlainText()

    if not user_id or not username or not password:
        QMessageBox.warning(window, "Missing Info", "Please fill in all user fields.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (UserID, Username, Password) VALUES (?, ?, ?)", (user_id, username, password))
        conn.commit()
        conn.close()
        QMessageBox.information(window, "Added", f"User '{username}' added successfully.")
        window.load_users()
    except sqlite3.IntegrityError:
        QMessageBox.warning(window, "Conflict", f"User ID {user_id} already exists.")
    except sqlite3.Error as e:
        QMessageBox.critical(window, "Database Error", str(e))

def update_user(window):
    selected = window.tableUsers.selectedItems()
    if not selected:
        QMessageBox.warning(window, "No Selection", "Please select a user to update.")
        return

    user_id = selected[0].text()
    new_username = window.UsernameTextbox.toPlainText() 
    new_password = window.PasswordTextbox.toPlainText() 
    new_userid = window.UseridTextbox.toPlainText()

    if not new_userid or not new_username or not new_password:
        QMessageBox.warning(window, "Missing Info", "Please fill in all fields.")
        return 

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Users SET Username = ?, Password = ?, UserID = ? WHERE UserID = ?",
            (new_username, new_password, new_userid, user_id)
        )
        conn.commit()
        conn.close()
        QMessageBox.information(window, "Updated", f"User ID {user_id} updated successfully.")
        window.load_users()
    except sqlite3.Error as e:
        QMessageBox.critical(window, "Database Error", str(e))
