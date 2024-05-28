import sys
import csv
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("dsaUI/UI.ui", self)

        # For placeholder text
        self.plainTextEdit.setPlainText("Username")
        self.plainTextEdit_2.setPlainText("Password")
        self.plainTextEdit_3.setPlainText("Admin/User")

        # Connecting the button click event to the storeInfo method
        self.pushButton.clicked.connect(self.storeInfo)

    def hashPassword(self, password):
        hash_object = hashlib.sha256(password.encode())
        hash_data = hash_object.hexdigest()
        return hash_data

    def storePassword(self, hash_data, username, role):
        with open("passwords.csv", mode="a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([username, hash_data, role])

    def checkPassword(self, hash_data):
        with open("passwords.csv", mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row and row[1] == hash_data:
                    return True
        return False

    def storeInfo(self):
        # Retrieving text from the plain text edits
        username = self.plainTextEdit.toPlainText()
        password = self.plainTextEdit_2.toPlainText()
        role = self.plainTextEdit_3.toPlainText()

        # Hash the password
        hash_data = self.hashPassword(password)

        # Check if the password already exists
        if self.checkPassword(hash_data):
            msg = "username or password is already exist"
            QMessageBox.information(self, "Information Saved", msg)
        else:
            # Store the user information
            self.storePassword(hash_data, username, role)
            msg = "Data stored successfully"
            QMessageBox.information(self, "Information Saved", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
