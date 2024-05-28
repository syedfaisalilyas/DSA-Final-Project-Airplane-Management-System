import sys
import csv
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("dsaUI/untitled.ui", self)

        # For placeholder text
        self.plainTextEdit_4.setPlainText("Flight#")
        self.plainTextEdit_8.setPlainText("Airline")
        self.plainTextEdit_9.setPlainText("DepartureCity")
        self.plainTextEdit_10.setPlainText("DestinationCity")
        self.plainTextEdit_5.setPlainText("TotalSeats")
        self.plainTextEdit_6.setPlainText("price")

        # Connecting the button 
        self.pushButton_9.clicked.connect(self.storeInfo)
    
    def storeDataToCsv(self, Flightno, Airline, DepartureCity,DestinationCity,DestinaltionTime,DepartureTimeTime,TotalSeats,Price,Class):
        
        with open("booking.csv", mode="a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([Flightno, Airline, DepartureCity,DestinationCity,DestinaltionTime,DepartureTimeTime,TotalSeats,Price,Class])

    def storeInfo(self):
        # Retrieving text from the plain text edits
        Flightno = self.plainTextEdit_4.toPlainText()
        Airline = self.plainTextEdit_8.toPlainText()
        DepartureCity = self.plainTextEdit_9.toPlainText()
        DestinationCity = self.plainTextEdit_10.toPlainText()
        DestinationTime = self.timeEdit.time().toString()
        DepartureTimeTime = self.timeEdit_2.time().toString()
        TotalSeats = self.plainTextEdit_5.toPlainText()
        Price = self.plainTextEdit_6.toPlainText()
        Class = self.comboBox.currentText()
        
        if (Price == "price" or Price == "") and(TotalSeats == "TotalSeats" or TotalSeats == "") and (DestinationCity == "DestinationCity" or DestinationCity == "") and (DepartureCity== "DepartureCity" or DepartureCity == "") and(DepartureCity == "DepartureCity" or DepartureCity == "")and(Flightno == "Flight#" or Flightno == "") and (Airline == "Airline" or Airline == ""):
            msg = "Please put valid data"
            QMessageBox.information(self, "Information Saved", msg)
            
        else:
            #Call funtion to store data
            self.storeDataToCsv(Flightno, Airline, DepartureCity,DestinationCity,DestinationTime,DepartureTimeTime,TotalSeats,Price,Class)
            msg = "Data stored successfully"
            QMessageBox.information(self, "Information Saved", msg)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
