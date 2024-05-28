from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox
import sys
from linked_list import LinkedList
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.centralLayout.addWidget(self.background)
        
        # Header
        self.label = QtWidgets.QLabel("Admin Menu", self.centralwidget)
        self.label.setStyleSheet("background-color: rgba(255, 204, 153, 150); font: 20pt 'Arial Rounded MT Bold';")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.centralLayout.addWidget(self.label)

        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.centralLayout.addWidget(self.gridWidget)   

        # Table to show the data
        self.tableWidget = QtWidgets.QTableWidget(self.gridWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Passenger ID", "Name", "Email", "Phone"])
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: rgba(255, 204, 153, 150); }")  # Light orange header
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)

        # Buttons Creation
        self.pushButton_add_user = QtWidgets.QPushButton("Add User", self.centralwidget)
        self.pushButton_remove_user = QtWidgets.QPushButton("Remove User", self.centralwidget)
        self.pushButton_update_user = QtWidgets.QPushButton("Update User", self.centralwidget)

        button_styles = "background-color: red; color: white; border-radius: 5px;"
        for btn in (self.pushButton_add_user, self.pushButton_remove_user, self.pushButton_update_user):
            btn.setStyleSheet(button_styles)
            btn.setFixedSize(200, 30)

        self.pushButton_add_user.clicked.connect(self.add_user)
        self.pushButton_remove_user.clicked.connect(self.remove_user)
        self.pushButton_update_user.clicked.connect(self.update_user)

        layout = self.centralwidget.layout()
        button_layout = QtWidgets.QHBoxLayout()

        button_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        button_layout.addWidget(self.pushButton_add_user)
        button_layout.addWidget(self.pushButton_remove_user)
        button_layout.addWidget(self.pushButton_update_user)
        button_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        layout.addLayout(button_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        table_stylesheet = (
            "QTableWidget {"
            "background-color: rgba(255, 204, 153, 150);"
            "border: none;"
            "}"
            "QTableWidget::item:selected {"
            "background-color: #FF9966;"
            "}"
        )
        self.tableWidget.setStyleSheet(table_stylesheet)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: rgba(255, 204, 153, 150); }")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    # Function to laod data into the table
    def load_data_into_grid(self, data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_idx, col_idx, item)

    # Function to load data from the file
    def load_data_from_file(self,file_path):
        data = read_data_from_csv(file_path)
        self.load_data_into_grid(data)

    # Get data from the table for operations
    def get_table_data(self):
        data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                cell_text = self.tableWidget.item(row, col).text()
                row_data.append(cell_text)
            data.append(row_data)
        return data    

    # Funcion of adding new user
    def add_user(self):
            name, ok = QInputDialog.getText(self.centralwidget, "Add User", "Enter Name:")
            if ok:
                email, ok = QInputDialog.getText(self.centralwidget, "Add User", "Enter Email:")
                if ok:
                    phone, ok = QInputDialog.getText(self.centralwidget, "Add User", "Enter Phone:")
                    if ok:
                        id, ok = QInputDialog.getText(self.centralwidget,"Add User", "Enter ID:")
                        if ok:
                            user_data = {"Passenger ID": id, "Name": name, "Email": email, "Phone": phone}
                            self.linked_list.append(user_data)  # Add to the linked list

                        current_row = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(current_row)

                        self.tableWidget.setItem(current_row, 0, QTableWidgetItem(user_data["Passenger ID"]))
                        self.tableWidget.setItem(current_row, 1, QTableWidgetItem(user_data["Name"]))
                        self.tableWidget.setItem(current_row, 2, QTableWidgetItem(user_data["Email"]))
                        self.tableWidget.setItem(current_row, 3, QTableWidgetItem(user_data["Phone"]))

    # Function for removing the user
    def remove_user(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self.centralwidget, "Warning", "No user selected for removal.")
            return

        for row in selected_rows:
            passenger_id = self.tableWidget.item(row.row(), 0).text()
            self.linked_list.remove({"Passenger ID": passenger_id})  # Remove from the linked list
            self.tableWidget.removeRow(row.row())

    # Function for updating information of existing user
    def update_user(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self.centralwidget, "Warning", "No user selected for update.")
            return

        name, ok = QInputDialog.getText(self.centralwidget, "Update User", "Enter Name:")
        if not ok:
            return
        email, ok = QInputDialog.getText(self.centralwidget, "Update User", "Enter Email:")
        if not ok:
            return
        phone, ok = QInputDialog.getText(self.centralwidget, "Update User", "Enter Phone:")
        if not ok:
            return
        id, ok = QInputDialog.getText(self.centralwidget, "Update User", "Enter ID:")
        if not ok:
            return

        for row in selected_rows:
            current_row = row.row()
            old_passenger_id = self.tableWidget.item(current_row, 0).text()

            self.tableWidget.setItem(current_row, 0, QTableWidgetItem(id))
            self.tableWidget.setItem(current_row, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(current_row, 2, QTableWidgetItem(email))
            self.tableWidget.setItem(current_row, 3, QTableWidgetItem(phone))

    # Function for re-running whole UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Menu"))        
      

# Function to read data from a CSV file
def read_data_from_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return data

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.linked_list = LinkedList()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.load_data_from_file('flight_booking_data_passengers.csv')
    sys.exit(app.exec_())