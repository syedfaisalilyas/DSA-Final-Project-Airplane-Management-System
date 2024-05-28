from FlightCrudLinkedList import *
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("crud.ui", self)

        file_path = 'planes_data.csv'
        flight_list = FlightLinkedList()
        self.load_flights_from_csv(file_path, flight_list)

        print("Flights from CSV:")
        flight_list.display_flights()
        fn, ft, pn, c, ss, dd, d, du=self.getList(flight_list)
        self.populate_table(fn, ft, pn, c, ss, dd, d, du)
        self.addBt.clicked.connect(lambda: self.addFlight(flight_list))
        self.delete_bt.clicked.connect(self.remove_selected_row)

    def write_to_csv( self,*lists):
        with open('planes_data.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the header if needed
            # csv_writer.writerow(['Header1', 'Header2', ...])

            # Write each list as a separate row
            for row in zip(*lists):
                csv_writer.writerow(row)


    def remove_selected_row(self):
        # Get data from the selected row
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setStyleSheet("QLabel{ color: white; } QMessageBox{ background-color: white; }")
            msg_box.warning(self, "Warning", "No row selected.")
        else:
            for row in selected_rows:
                fNumber = self.tableWidget.item(row.row(), 0).text()
                fType = self.tableWidget.item(row.row(), 1).text()
                pName = self.tableWidget.item(row.row(), 2).text()
                capacity = self.tableWidget.item(row.row(), 3).text()
                src = self.tableWidget.item(row.row(), 4).text()
                dest = self.tableWidget.item(row.row(), 5).text()
                date = self.tableWidget.item(row.row(), 6).text()
                duration = self.tableWidget.item(row.row(), 7).text()

                # Remove the selected row from the table
                self.tableWidget.removeRow(row.row())

                print(f"Flight Number: {fNumber}")
                print(f"Flight Type: {fType}")
                print(f"Passenger Name: {pName}")
                print(f"Capacity: {capacity}")
                print(f"Source: {src}")
                print(f"Destination: {dest}")
                print(f"Date: {date}")
                print(f"Duration: {duration}")


    def getSelectedRowData(self):
        # Get data from the selected row
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QtWidgets.QMessageBox.warning(self, "Warning", "No row selected.")
        else:
            for row in selected_rows:
                fNumber = self.tableWidget.item(row.row(), 0).text()
                fType = self.tableWidget.item(row.row(), 1).text()
                pName = self.tableWidget.item(row.row(), 2).text()
                capacity = self.tableWidget.item(row.row(), 3).text()
                src = self.tableWidget.item(row.row(), 4).text()
                dest = self.tableWidget.item(row.row(), 5).text()
                date = self.tableWidget.item(row.row(), 6).text()
                duration = self.tableWidget.item(row.row(), 7).text()
                print(f"Flight Number: {fNumber}")
                print(f"Flight Type: {fType}")
                print(f"Passenger Name: {pName}")
                print(f"Capacity: {capacity}")
                print(f"Source: {src}")
                print(f"Destination: {dest}")
                print(f"Date: {date}")
                print(f"Duration: {duration}")

    def getList(self,flight_list):
        current = flight_list.head
        fn=[]
        ft=[]
        pn=[]
        c=[]
        ss=[]
        dd=[]
        d=[]
        du=[]
        while current:
            fn.append(current.fNumber)
            ft.append(current.fType)
            pn.append(current.pName)
            c.append(current.capacity)
            ss.append(current.src)
            dd.append(current.dest)
            d.append(current.date)
            du.append(current.duration)
            current = current.next
        return fn,ft,pn, c,ss,dd,d,du


    def addFlight(self,flight_list):
        fNumber, fType, pName, capacity, src, dest, date, duaration = self.getInput()
        flight_list.append_flight(fNumber,fType,pName,capacity,src,dest,date,duaration)
        print("Updated Flights:")
        flight_list.display_flights()
        fn, ft, pn, c, ss, dd, d, du=self.getList(flight_list)
        self.populate_table(fn,ft,pn, c,ss,dd,d,du)
        self.write_to_csv(fn,ft,pn, c,ss,dd,d,du)
    def getInput(self):
        fNumber=self.number_txt.text()
        pName=self.pName.text()
        date=self.date_txt.text()
        src=self.ss.text()
        dest=self.dd.text()
        duaration=self.duaration_txt.text()
        fType=self.fType_txt.currentText()
        capacity=self.capacity_txt.text()
        return fNumber,fType,pName,capacity,src,dest,date,duaration

    def load_flights_from_csv(self,file_path, flight_list):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_list.add_flight(
                    row['fNumber'],
                    row['fType'],
                    row['pName'],
                    int(row['capacity']),
                    row['src'],
                    row['dest'],
                    row['date'],
                    row['duration']
                )

    def populate_table(self, Name, Price, Description, Ratings, NoOfReviews, DiscountedPrice, Delivery, perOff):
        # Clear the existing items in the tableWidget (optional)
        self.tableWidget.clearContents()

        # Assuming len(Name) is the number of rows
        num_rows = len(Name)
        self.tableWidget.setRowCount(num_rows)

        for row in range(num_rows):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Name[row])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Price[row])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Description[row])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Ratings[row])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(NoOfReviews[row])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(DiscountedPrice[row])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Delivery[row])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(perOff[row])))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
