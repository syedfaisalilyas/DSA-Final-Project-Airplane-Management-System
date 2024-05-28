import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from register import RegistrationWindow
import subprocess
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login")
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
        title_label = QLabel("Login", overlay)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: black; font-size: 50px; font-weight: bold;")  # Black text, larger font
        overlay_layout.addWidget(title_label)

        # Create line edits for username, password
        self.username_edit = QLineEdit(overlay)
        self.username_edit.setPlaceholderText("Username")
        self.username_edit.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.username_edit)

        self.password_edit = QLineEdit(overlay)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setStyleSheet("font-size: 16px; padding: 8px;background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.password_edit)

        # Add checkbox for showing/hiding password
        self.show_password_checkbox = QCheckBox("Show Password", overlay)
        self.show_password_checkbox.setStyleSheet("font-size: 16px; color: black;")  # Checkbox styling
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        overlay_layout.addWidget(self.show_password_checkbox, alignment = Qt.AlignRight)

        # Create combo box for role selection
        self.role_combobox = QComboBox(overlay)
        self.role_combobox.addItems(["User", "Admin"])
        self.role_combobox.setStyleSheet("font-size: 16px; padding: 8px; background-color: rgba(255, 204, 153, 100);")  # Light orange background
        overlay_layout.addWidget(self.role_combobox)

        # Add a login button with reduced size
        login_button = QPushButton("     Login     ", overlay)
        login_button.setStyleSheet("font-size: 18px; padding: 10px 20px; max-width: 200px; background-color: red; color: white; font-weight: bold;")  # Dark orange button
        overlay_layout.addWidget(login_button, alignment=Qt.AlignCenter)
        login_button.clicked.connect(self.handle_login)

        # Add a label and a button for registration closer together
        register_label = QLabel("Don't have an account?", overlay)
        register_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        register_label.setStyleSheet("color: black; font-size: 20px;")  # Smaller font
        overlay_layout.addWidget(register_label)

        register_button = QPushButton("     Register     ", overlay)
        register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;  max-width: 100px; background-color: red; color: white; font-weight: bold;")  # Dark orange button
        overlay_layout.addWidget(register_button,  alignment=Qt.AlignCenter)
        register_button.clicked.connect(self.show_registration)


    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        role = self.role_combobox.currentText()

        if not (username and password and role):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
            return

        try:
            with open('registrations.csv', mode='r') as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if row[0] == username and row[1] == password and row[4] == role:
                        found = True
                        if role == 'Admin':
                            QMessageBox.information(self, 'Login Successful', 'Welcome, Admin!')
                            self.showAdmin()
                        else:
                            QMessageBox.information(self, 'Login Successful', 'Welcome, User!')
                            self.showUser()
                        break

                if not found:
                    QMessageBox.warning(self, 'Error', 'Invalid user')
        except Exception as e:
            print(f"Error: {e}")


    def show_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

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

    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
