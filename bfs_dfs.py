import tkinter as tk
from tkinter import ttk
import pandas as pd
from collections import defaultdict, deque

# Load the CSV file into a DataFrame
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Assuming 'Source_Country' and 'Destination_Country' represent edges in the graph
graph = defaultdict(list)

# Create an adjacency list representation of the graph
for _, row in data.iterrows():
    src = row['Source_Country']
    dest = row['Destination_Country']
    graph[src].append(dest)
    graph[dest].append(src)  # If graph is undirected

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))

    return traversal

def run_bfs():
    start_node = start_entry.get()
    bfs_traversal = bfs(graph, start_node)
    bfs_result_text.delete(1.0, tk.END)
    bfs_result_text.insert(tk.END, "\n".join(bfs_traversal))

def run_dfs():
    start_node = start_entry.get()
    dfs_traversal = dfs(graph, start_node)
    dfs_result_text.delete(1.0, tk.END)
    dfs_result_text.insert(tk.END, "\n".join(dfs_traversal))

root = tk.Tk()
root.title("Graph Traversal")
root.configure(bg='#6417ff')  # Setting the background color to rgb(100, 23, 255)

# Styling
style = ttk.Style()
style.theme_use('vista')  # Choose a theme (other options: 'default', 'alt', 'classic', 'vista')

# Create UI elements
title_label = ttk.Label(root, text="Graph Traversal", font=('Arial', 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

start_label = ttk.Label(root, text="Enter Starting Node:")
start_label.grid(row=1, column=0, padx=5, pady=5)

start_entry = ttk.Entry(root)
start_entry.grid(row=1, column=1, padx=5, pady=5)

bfs_button = ttk.Button(root, text="Run BFS", command=run_bfs)
bfs_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

dfs_button = ttk.Button(root, text="Run DFS", command=run_dfs)
dfs_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

bfs_result_label = ttk.Label(root, text="BFS Traversal:")
bfs_result_label.grid(row=4, column=0, padx=5, pady=5)

bfs_result_text = tk.Text(root, height=20, width=40)
bfs_result_text.grid(row=5, column=0, padx=5, pady=5)

dfs_result_label = ttk.Label(root, text="DFS Traversal:")
dfs_result_label.grid(row=4, column=1, padx=5, pady=5)

dfs_result_text = tk.Text(root, height=20, width=40)
dfs_result_text.grid(row=5, column=1, padx=5, pady=5)

def close_window():
    root.attributes('-fullscreen', False)  # Disable full screen
    root.destroy()  # Close the window

close_button = ttk.Button(root, text="Close", command=close_window)
close_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

def escape_key(event):
    if event.keysym == 'Escape':
        root.attributes('-fullscreen', False)  # Disable full screen
        root.destroy()  # Close the window

root.bind('<Key>', escape_key)  # Bind the escape key event to the function


# Configure row and column weights to make the grid responsive
root.grid_rowconfigure(5, weight=1)
root.attributes('-fullscreen', True)
root.grid_columnconfigure((0, 1), weight=1)

root.mainloop()
