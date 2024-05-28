import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("adminMainUI.ui", self)

        # Connect each button to its corresponding function
        self.addUser.clicked.connect(self.run_script)
        self.graph_bt.clicked.connect(self.run_script)
        self.serachFlights.clicked.connect(self.run_script)
        self.addFlight.clicked.connect(self.run_script)
        self.serachUsers.clicked.connect(self.run_script)
        self.graph_bt_2.clicked.connect(self.run_script)
        self.sortFlights_bt.clicked.connect(self.run_script)

    def run_script(self):
        sender_button = self.sender()
        try:
            if sender_button == self.addUser:
                script_path = "Add_Remove_User.py"
            elif sender_button == self.graph_bt:
                script_path = "graph.py"
            elif sender_button == self.serachFlights:
                script_path = "multiLevelSearching.py"
            elif sender_button == self.addFlight:
                script_path = "Add_Remove_Plane.py"
            elif sender_button == self.serachUsers:
                script_path = "searchUsers.py"
            elif sender_button == self.graph_bt_2:
                script_path = "all_graph_types.py"
            elif sender_button == self.sortFlights_bt:
                script_path = "sorting.py"
            else:
                return

            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:

            print(f"Error running script: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
