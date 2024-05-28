import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from BST import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5.QtGui import QColor
import AVLTree as avl
from RedBlack import *


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.resize(903, 582)
        loadUi("singleLevelSearching.ui", self)
        self.load_DataFromFile()
        self.searchButton.clicked.connect(self.searchButtonClick)
    def searchButtonClick(self):
        self.clearHighlightedRows()
        selected_choice = self.choice.currentText()
        print(f"Selected item: {selected_choice}")
        selected_column = self.columnBox.currentText()
        print(f"Selected item: {selected_column}")
        searchQuery = self.query.text()
        print(f"Selected item: {searchQuery}")
        sType = self.searchingType.currentText()
        fNumber, ftype, pName, capacity, sCountry, dCountry, date, duaration = self.getDataFromTable()
        listToSearch = []
        if selected_column == "FlightNumber":
            listToSearch = fNumber
        elif selected_column == "FlightType":
            listToSearch = ftype
        elif selected_column == "PilotName":
            listToSearch = pName
        elif selected_column == "Capacity":
            listToSearch = capacity
        elif selected_column == "SourceCountry":
            listToSearch = sCountry
        elif selected_column == "DestinationCountry":
            listToSearch = dCountry
        elif selected_column == "Date":
            listToSearch = date
        elif selected_column == "Duaration":
            listToSearch = duaration
        searched = []
        bst_root = None
        avl_root = None
        rb_tree = RBTree()
        for value in listToSearch:
            if sType == "BST":
                bst_root = insert_bst(bst_root, value)
            elif sType == "RB":
                rb_insert(rb_tree, value)
            else:
                avl_root = avl.insert_avl(avl_root, value)
        if selected_choice == "StartsWith":
            if sType == "BST":
                searched = startsWith_BST(bst_root, searchQuery)
            elif sType == "RB":
                searched = startsWith_RB(rb_tree, searchQuery)
            else:
                searched = avl.startsWith_AVL(avl_root, searchQuery)
        elif selected_choice == "EndWith":
            if sType == "BST":
                searched = endWith_BST(bst_root, searchQuery)
            elif sType == "RB":
                searched = endWith_RB(rb_tree, searchQuery)
            else:
                searched = avl.endWith_AVL(avl_root, searchQuery)
        elif selected_choice == "Contains":
            if sType == "BST":
                searched = contains_BST(bst_root, searchQuery)
            elif sType == "RB":
                searched = contains_RB(rb_tree, searchQuery)
            else:
                searched = avl.contains_AVL(avl_root, searchQuery)
        print(searched)
        selected = self.getMatchingRows(listToSearch, searched)
        self.highlightRows(selected)

    def getMatchingRows(self, listToSearch, searched):
        selected = []
        for i in range(len(listToSearch)):
            # print(searched[i])
            for j in range(len(searched)):
                if searched[j] == listToSearch[i]:
                    selected.append(i)
        return selected

    def clearHighlightedRows(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(QColor(23, 107, 135))

    def highlightRows(self, selected):
        for row in selected:
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(QColor(255, 0, 0))

    def load_DataFromFile(self):
        with open("Example.csv", 'r', encoding='iso-8859-1',
                  errors='replace') as fileInput:
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.tableWidget.setRowCount(len(self.data))
            for row in self.data:
                self.tableWidget.setItem(
                    tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.tableWidget.setItem(
                    tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.tableWidget.setItem(
                    tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.tableWidget.setItem(
                    tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.tableWidget.setItem(
                    tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.tableWidget.setItem(
                    tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.tableWidget.setItem(
                    tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.tableWidget.setItem(
                    tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))

                tableRows += 1

    def load_Data(self):
        tableRows = 0
        self.tableWidget.setRowCount(len(self.data))
        for row in self.data:
            self.tableWidget.setItem(
                tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.tableWidget.setItem(
                tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.tableWidget.setItem(
                tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.tableWidget.setItem(
                tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.tableWidget.setItem(
                tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            # if int(row[5].split(":")[0]) >= int(24):
            #     row[5] = row[5][0:len(row[5])-1]
            self.tableWidget.setItem(
                tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            self.tableWidget.setItem(
                tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
            self.tableWidget.setItem(
                tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
            tableRows += 1

    def getDataFromTable(self):
        fNumber = []
        ftype = []
        pName = []
        capacity = []
        sCountry = []
        dCountry = []
        date = []
        duaration = []
        for row in self.data:
            fNumber.append(row[0])
            ftype.append(row[1])
            pName.append(row[2])
            capacity.append(row[3])
            sCountry.append(row[4])
            dCountry.append(row[5])
            date.append(row[6])
            duaration.append(row[7])
        return fNumber, ftype, pName, capacity, sCountry, dCountry, date, duaration

        # Now, you have separate lists for each column of data

app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
