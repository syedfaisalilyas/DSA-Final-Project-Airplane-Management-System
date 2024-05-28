import sys
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from BST import *
import AVLTree as avl
from RedBlack import *
import tkinter as tk
from tkinter import messagebox


class Mainwindow(QMainWindow):
    def __init__(self):

        super(Mainwindow, self).__init__()
        self.resize(903, 582)
        loadUi("searchUsers.ui", self)

        self.load_DataFromFile("Example.csv")
        self.searchButton.clicked.connect(self.search_button_click)

    def search_button_click(self):
        self.clearHighlightedRows()
        selected_algo = self.algo.currentText()
        print(f"Selected item: {selected_algo}")
        selectedType = self.type.currentText()
        print(selectedType)
        selectedOrder = self.order.currentText()
        print(selectedOrder)
        sType = self.searchingType.currentText()
        searchQuery = self.query.text()
        print(searchQuery)
        fNumber, ftype, pName, capacity, sCountry, dCountry, date, duaration = self.getDataFromTable()

        lists = []
        checkedBoxes = self.getCheckBoxes()
        for i in range(len(checkedBoxes)):
            if checkedBoxes[i] == "FlightNumber":
                lists.append(fNumber)
            elif checkedBoxes[i] == "FlightType":
                lists.append(ftype)
            elif checkedBoxes[i] == "PilotName":
                lists.append(pName)
            elif checkedBoxes[i] == "Capacity":
                lists.append(capacity)
            elif checkedBoxes[i] == "SourceCountry":
                lists.append(sCountry)
            elif checkedBoxes[i] == "DestinationCountry":
                lists.append(dCountry)
            elif checkedBoxes[i] == "Date":
                lists.append(date)
            elif checkedBoxes[i] == "Duaration":
                lists.append(duaration)
        # try:
        #     checkedBoxes = self.getCheckBoxes()
        #     # Check if searchQuery is not empty
        #     if len(checkedBoxes<2):
        #         raise ValueError("Please select at least 2 check boxes")

        # except ValueError as ve:
        #     print(f"ValueError: {ve}")
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        #     messagebox.showerror("Error", str(e))

        searched = []
        bst_root = None
        avl_root = None
        rb_tree = RBTree()
        try:
            searchQuery = self.query.text()
            # Check if searchQuery is not empty
            if not searchQuery:
                raise ValueError("Search query cannot be empty")
            # Your code that uses searchQuery
            for singleList in lists:
                if sType == "BST":
                    for value in singleList:
                        bst_root = insert_bst(bst_root, value)
                    if selectedType == "Contains":
                        searched.append(contains_BST(bst_root, searchQuery))
                    elif selectedType == "StartsWith":
                        searched.append(startsWith_BST(bst_root, searchQuery))
                    elif selectedType == "EndWith":
                        searched.append(endWith_BST(bst_root, searchQuery))
                elif sType == "AVL":
                    for value in singleList:
                        avl_root =  avl.insert_avl(avl_root, value)
                    if selectedType == "Contains":
                        searched.append(avl.contains_AVL(avl_root, searchQuery))
                    elif selectedType == "StartsWith":
                        searched.append(avl.startsWith_AVL(avl_root, searchQuery))
                    elif selectedType == "EndWith":
                        searched.append(avl.endWith_AVL(avl_root, searchQuery))
                elif sType == "RB":
                    for value in singleList:
                        rb_insert(rb_tree, value)
                    if selectedType == "Contains":
                        searched.append(contains_RB(rb_tree, searchQuery))
                    elif selectedType == "StartsWith":
                        searched.append(startsWith_RB(rb_tree, searchQuery))
                    elif selectedType == "EndWith":
                        searched.append(endWith_RB(rb_tree, searchQuery))

            mainList = []

            for i in range(len(searched)):
                mainList.append(self.getMatchingRows(lists[i], searched[i]))
            min_length = float('inf')

            max_length = 0
            min_length_index = None
            max_length_index = None
            other_lengths = []
            other_lists = []
            other_indices = []

            for index, sublist in enumerate(mainList):
                sublist_length = len(sublist)
                if sublist_length < min_length:
                    min_length = sublist_length
                    min_length_index = index
                if sublist_length > max_length:
                    max_length = sublist_length
                    max_length_index = index
                if sublist_length != max_length or sublist_length != min_length:
                    other_lengths.append(sublist_length)
                    other_lists.append(sublist)
                    other_indices.append(index)

            print("LENGTH OF MAIN LIST", len(mainList))
            if len(mainList) == 2:
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                set1 = set(col0)
                set2 = set(col1)
                if selectedOrder == "AND":
                    intersection = set1.intersection(set2)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set1.union(set2)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set1 - set2
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 3:
                print(other_indices[0])
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 4:
                print(other_indices[0])
                print(other_indices[1])
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                col3 = mainList[other_indices[1]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                set3 = set(col3)
                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1, set3)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1, set3)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2 - set3
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 5:
                print(other_indices[0])
                print(other_indices[1])
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                col3 = mainList[other_indices[1]]
                col4 = mainList[other_indices[2]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                set3 = set(col3)
                set4 = set(col4)
                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1, set3, set4)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1, set3, set4)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2 - set3 - set4
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 6:
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                col3 = mainList[other_indices[1]]
                col4 = mainList[other_indices[2]]
                col5 = mainList[other_indices[3]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                set3 = set(col3)
                set4 = set(col4)
                set5 = set(col5)
                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1, set3, set4)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1, set3, set4, set5)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2 - set3 - set4 - set5
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 7:
                print(other_indices[0])
                print(other_indices[1])
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                col3 = mainList[other_indices[1]]
                col4 = mainList[other_indices[2]]
                col5 = mainList[other_indices[3]]
                col6 = mainList[other_indices[4]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                set3 = set(col3)
                set4 = set(col4)
                set5 = set(col5)
                set6 = set(col6)

                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1, set3, set4, set5, set6)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1, set3, set4, set5, set6)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2 - set3 - set4 - set5 - set6
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
            elif len(mainList) == 8:
                print(other_indices[0])
                print(other_indices[1])
                print(max_length_index)
                print(min_length_index)
                col0 = mainList[min_length_index]
                col1 = mainList[max_length_index]
                col2 = mainList[other_indices[0]]
                col3 = mainList[other_indices[1]]
                col4 = mainList[other_indices[2]]
                col5 = mainList[other_indices[3]]
                col6 = mainList[other_indices[4]]
                col7 = mainList[other_indices[5]]
                set0 = set(col0)
                set1 = set(col1)
                set2 = set(col2)
                set3 = set(col3)
                set4 = set(col4)
                set5 = set(col5)
                set6 = set(col6)
                set7 = set(col7)

                if selectedOrder == "AND":
                    intersection = set0.intersection(set2, set1, set3, set4, set5, set6, set7)
                    # Convert the result back to a list
                    intersection_list = list(intersection)
                    self.highlightRows(intersection_list)
                elif selectedOrder == "OR":
                    union = set0.union(set2, set1, set3, set4, set5, set6, set7)
                    unionList = list(union)
                    self.highlightRows(unionList)
                else:
                    negation_result = set0 - set1 - set2 - set3 - set4 - set5 - set6 - set7
                    negationList = list(negation_result)
                    self.highlightRows(negationList)
        except ValueError as ve:
            print(f"ValueError: {ve}")
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            print(f"An error occurred: {e}")
            messagebox.showerror("Error", str(e))





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
                item.setBackground(QColor(255, 0, 0))  # Set the background color (here, it's red)

    def getCheckBoxes(self):
        checked_checkboxes = []

        if self.fNumber.isChecked():
            checked_checkboxes.append("FlightNumber")
        if self.ftype.isChecked():
            checked_checkboxes.append("FlightType")
        if self.pName.isChecked():
            checked_checkboxes.append("PilotName")
        if self.capacity.isChecked():
            checked_checkboxes.append("Capacity")
        if self.sCountry.isChecked():
            checked_checkboxes.append("SourceCountry")
        if self.dCountry.isChecked():
            checked_checkboxes.append("DestinationCountry")
        if self.date.isChecked():
            checked_checkboxes.append("Date")
        if self.duaration.isChecked():
            checked_checkboxes.append("Duaration")
        # print("Checked checkboxes:", checked_checkboxes)
        return checked_checkboxes

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

    def load_DataFromFile(self,path):
        with open(path, 'r', encoding='iso-8859-1',
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


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
