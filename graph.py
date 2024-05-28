import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

import subprocess
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("IntegratedGraphs.ui", self)

        # Connect each button to its corresponding function
        self.line.clicked.connect(self.run_line_graph_script)
        self.bar.clicked.connect(self.run_bar_graph_script)
        self.pie.clicked.connect(self.run_pie_graph_script)
        self.scatter.clicked.connect(self.run_scatter_graph_script)
        self.prim_bt.clicked.connect(self.run_prims_script)
        self.kruskal_bt.clicked.connect(self.run_kruskal_script)
        self.bfs_dfs_bt.clicked.connect(self.run_bfs_dfs_script)

    def run_bfs_dfs_script(self):
        script_path = "bfs_dfs.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

    def run_line_graph_script(self):
        script_path = "linegraph.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")
    def run_pie_graph_script(self):
        # Replace "path/to/your/lineGraphScript.py" with the actual path to your script
        script_path = "piegraph.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")
    def run_scatter_graph_script(self):
        # Replace "path/to/your/lineGraphScript.py" with the actual path to your script
        script_path = "scattergraph.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

    def run_prims_script(self):
        script_path = "MST(prims).py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

    def run_kruskal_script(self):
        # Replace "path/to/your/lineGraphScript.py" with the actual path to your script
        script_path = "MST(kruskal).py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")
    def run_bar_graph_script(self):
        # Replace "path/to/your/lineGraphScript.py" with the actual path to your script
        script_path = "bargraph.py"

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors that might occur while running the script
            print(f"Error running script: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())