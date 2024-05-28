from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox
import sys

# Define the Plane class
class Plane:
    def __init__(self, flight_number, flight_type, pilot_name, capacity, source_country, destination_country, date, time):
        self.flight_number = flight_number
        self.flight_type = flight_type
        self.pilot_name = pilot_name
        self.capacity = capacity
        self.source_country = source_country
        self.destination_country = destination_country
        self.date = date
        self.time = time
        self.prev = None
        self.next = None

# Define the Doubly Linked List for planes
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_plane(self, plane):
        if not self.head:
            self.head = plane
            self.tail = plane
        else:
            plane.prev = self.tail
            self.tail.next = plane
            self.tail = plane

    def remove_plane(self, flight_number):
        current = self.head
        while current:
            if current.flight_number == flight_number:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True
            current = current.next
        return False

# UI class for the application
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Remove the background image from the style sheet
        self.centralwidget.setStyleSheet("")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 760, 400))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Flight Number", "Flight Type", "Pilot Name", "Capacity", "Source Country", "Destination Country", "Date", "Time"]
        )
        self.tableWidget.setStyleSheet("background-color: rgba(255, 193, 102, 150);")  # Light orange color for the table

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setText("Add Plane")
        self.addButton.setStyleSheet("background-color: red; color: white;")  # Red color for the Add button
        self.addButton.clicked.connect(self.add_plane)

        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setText("Remove Plane")
        self.removeButton.setStyleSheet("background-color: red; color: white;")  # Red color for the Remove button
        self.removeButton.clicked.connect(self.remove_plane)

        # Using layouts to make the UI responsive
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.addButton)
        button_layout.addWidget(self.removeButton)

        main_layout.addWidget(self.tableWidget)
        main_layout.addLayout(button_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.plane_list = DoublyLinkedList()

    def add_plane(self):
        flight_number, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Flight Number:")
        if ok:
            flight_type, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Flight Type:")
            pilot_name, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Pilot Name:")
            capacity, ok = QInputDialog.getInt(self.centralwidget, "Add Plane", "Enter Capacity:")
            source_country, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Source Country:")
            destination_country, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Destination Country:")
            date, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Date:")
            time, ok = QInputDialog.getText(self.centralwidget, "Add Plane", "Enter Time:")

            new_plane = Plane(flight_number, flight_type, pilot_name, capacity, source_country, destination_country, date, time)
            self.plane_list.add_plane(new_plane)

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(new_plane.flight_number))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(new_plane.flight_type))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(new_plane.pilot_name))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(new_plane.capacity)))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(new_plane.source_country))
            self.tableWidget.setItem(row_position, 5, QTableWidgetItem(new_plane.destination_country))
            self.tableWidget.setItem(row_position, 6, QTableWidgetItem(new_plane.date))
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(new_plane.time))

    def remove_plane(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            flight_number = self.tableWidget.item(selected_row, 0).text()
            if self.plane_list.remove_plane(flight_number):
                self.tableWidget.removeRow(selected_row)
            else:
                QMessageBox.warning(self.centralwidget, "Warning", "Plane not found in the list.")
        else:
            QMessageBox.warning(self.centralwidget, "Warning", "Select a row to remove.")



    def read_plane_data_from_csv(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = [line.strip().split(',') for line in file.readlines()]
                return data
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []

    def load_plane_data_into_table(self, data):
        if not data or not data[0]:
            print("No data or empty data provided.")
            return
        
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    plane_data = ui.read_plane_data_from_csv('planes_data.csv')
    ui.load_plane_data_into_table(plane_data)
    MainWindow.show()
    sys.exit(app.exec_())
