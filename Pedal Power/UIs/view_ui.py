import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

DB_PATH = 'Database/pedalpower.db'

class ViewWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('UIs/view_ui.ui', self)
        self.setWindowTitle(f"Bike Records for User {user_id}")
        self.user_id = int(user_id)  # ✅ Filter based on passed user ID

        self.btnUpdateInfo.setEnabled(False)
        self.DistanceTextbox.setEnabled(False)
        self.DateTextbox.setEnabled(False)

        self.load_records()

        self.tableRecords.itemSelectionChanged.connect(self.on_record_selected)
        self.btnUpdateInfo.clicked.connect(self.update_record)
        self.btnRefreshv.clicked.connect(self.load_records)
        self.btnDone.clicked.connect(self.close)

    def load_records(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT RecordID, UserID, DistanceKM, RecordDate FROM BikeRecords WHERE UserID = ?", (self.user_id,))
            records = cursor.fetchall()
            conn.close()

            self.tableRecords.clearContents()
            self.tableRecords.setRowCount(len(records))
            self.tableRecords.setColumnCount(4)
            self.tableRecords.setHorizontalHeaderLabels(["Record ID", "User ID", "Distance (KM)", "Record Date"])

            for row_idx, record in enumerate(records):
                for col_idx, value in enumerate(record):
                    self.tableRecords.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except sqlite3.Error as e:
            print(f"Database error: {e}")

        self.btnUpdateInfo.setEnabled(False)
        self.DistanceTextbox.setEnabled(False)
        self.DateTextbox.setEnabled(False)
        self.DistanceTextbox.clear()
        self.DateTextbox.clear()

    def on_record_selected(self):
        has_selection = bool(self.tableRecords.selectedItems())
        self.btnUpdateInfo.setEnabled(has_selection)
        self.DistanceTextbox.setEnabled(has_selection)
        self.DateTextbox.setEnabled(has_selection)

    def update_record(self):
        selected = self.tableRecords.selectedItems()
        if selected:
            record_id = selected[0].text()
            new_distance = self.DistanceTextbox.text()
            new_date = self.DateTextbox.text()

            try:
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE BikeRecords
                    SET DistanceKM = ?, RecordDate = ?
                    WHERE RecordID = ?
                """, (new_distance, new_date, record_id))
                conn.commit()
                conn.close()
                print("Record updated successfully.")
                self.load_records()
            except sqlite3.Error as e:
                print(f"Update error: {e}")
