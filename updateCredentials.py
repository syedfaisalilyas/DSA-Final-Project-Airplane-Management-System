from FlightCrudLinkedList import *
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("updateCredentials2.ui", self)
        self.chk_bt.clicked.connect(self.checkCredentials)
    def checkCredentials(self):
        try:
            with open('registrations.csv', mode='r') as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if row[0] == self.name.text() and row[1] == self.password_txt.text():
                        found = True
                        self.close()
                        second_window = SecondWindow()
                        second_window.show()

                        break

                if not found:
                    QMessageBox.warning(self, 'Error', 'Invalid user')
        except Exception as e:
            print(f"Error: {e}")

    def showForDuration(self, duration):
        # Show the window
        self.show()

        # Set up a timer to close the window after the specified duration
        timer = QTimer(self)
        timer.timeout.connect(self.close)
        timer.start(duration)


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.resize(903, 582)
        loadUi("updateCredentials.ui", self)





if __name__ == '__main__':
    app = QApplication([])

    first_window = MainWindow()
    first_window.show()

    app.exec_()