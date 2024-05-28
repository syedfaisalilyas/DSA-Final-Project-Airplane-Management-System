import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
import subprocess
class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Register")
        self.setFixedSize(700, 800)  # Disable window resizing

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set background image
        pixmap = QPixmap('1234.jpg')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap.scaled(self.size()))  # Scale the image to window size
        background_label.setGeometry(0, 0, self.width(), self.height())

        # Create transparent overlay widget
        overlay = QWidget(self)
        overlay.setGeometry(0, 0, self.width(), self.height())

        # Create layout for overlay
        overlay_layout = QVBoxLayout(overlay)
        overlay_layout.setAlignment(Qt.AlignCenter)  # Align items to the center
        overlay_layout.setSpacing(40)

        # Add a label for the title
        title_label = QLabel("Register", overlay)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: black; font-size: 50px; font-weight: bold;")  # Black text, larger font
        overlay_layout.addWidget(title_label)

        # Create line edits for registration details
        self.username_edit = QLineEdit(overlay)
        self.username_edit.setPlaceholderText("Username")
        self.username_edit.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.username_edit)

        self.password_edit = QLineEdit(overlay)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.password_edit)

        self.show_password_checkbox = QCheckBox("Show Password", overlay)
        self.show_password_checkbox.setStyleSheet("font-size: 16px; color: black;")  # Checkbox styling
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        overlay_layout.addWidget(self.show_password_checkbox, alignment = Qt.AlignRight)

        self.age_edit = QLineEdit(overlay)
        self.age_edit.setPlaceholderText("Age")
        self.age_edit.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.age_edit)

        self.contact_edit = QLineEdit(overlay)
        self.contact_edit.setPlaceholderText("Contact")
        self.contact_edit.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.contact_edit)

        self.role_combobox = QComboBox(overlay)
        self.role_combobox.addItems(["User", "Admin"])
        self.role_combobox.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.role_combobox)


        # Add a register button
        register_button = QPushButton("     Register     ", overlay)
        register_button.setStyleSheet("font-size: 18px; padding: 10px 20px; max-width: 150px; background-color: red; color: white; font-weight: bold;")  # Dark orange button
        overlay_layout.addWidget(register_button, alignment=Qt.AlignCenter)
        register_button.clicked.connect(self.handle_registration)


    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)


    def handle_registration(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        age = self.age_edit.text()
        contact = self.contact_edit.text()
        role = self.role_combobox.currentText()

        if not all([username, password, age, contact, role]):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
            return

        try:
            with open('registrations.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, age, contact, role])
            QMessageBox.information(self, 'Success', 'Registration successful!')
            if role=="User":
                self.showUser()
            else:
                self.showAdmin()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
    def showUser(self):
        try:
            subprocess.run(["python", "userMainPage.py"], check=True)
        except subprocess.CalledProcessError as e:

            print(f"Error running script: {e}")
    def showAdmin(self):
        try:
            subprocess.run(["python", "adminMainPage.py"], check=True)
        except subprocess.CalledProcessError as e:

            print(f"Error running script: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())
