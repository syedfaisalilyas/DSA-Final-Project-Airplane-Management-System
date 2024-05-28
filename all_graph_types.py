import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

def draw_graph_with_title(graph, title, color):
    plt.figure(figsize=(10,7))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True, node_color=color, font_weight='normal')
    plt.title(title)
    plt.text(0.5, -0.1, title, ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.show()

# Create a directed graph
def run_directed_graph():
    directed_graph = nx.from_pandas_edgelist(
    data, source='Source_Country', target='Destination_Country', create_using=nx.DiGraph())
    draw_graph_with_title(directed_graph, 'Directed Graph', 'skyblue')


# Create an undirected graph
def run_undirected_graph():
    undirected_graph = nx.from_pandas_edgelist(
    data, source='Source_Country', target='Destination_Country'
    )
    draw_graph_with_title(undirected_graph, 'Undirected Graph', 'lightgreen')


# Create a pseudo graph (allows multiple edges between nodes)
def run_pseudo_graph():
    pseudo_graph = nx.MultiGraph()
    pseudo_graph.add_edges_from(
    zip(data['Source_Country'], data['Destination_Country'])
    )
    draw_graph_with_title(pseudo_graph, 'Pseudo Graph', 'lightcoral')


# Create a random graph for cyclic demonstration
def run_random_graph():
    random_graph = nx.gnm_random_graph(len(data), len(data) // 2)
    draw_graph_with_title(random_graph, 'Random Graph (Cyclic Demo)', 'lightpink')

# Create a complete graph
def run_complete_graph():    
    complete_graph = nx.complete_graph(len(data))
    draw_graph_with_title(complete_graph, 'Complete Graph', 'lightyellow')

    
def run_connected_graph():
    try:
    # Create a connected graph
        connected_graph = nx.connected_watts_strogatz_graph(10, 3, 0.1)
        draw_graph_with_title(connected_graph, 'Connected Graph', 'lightgray')
    except Exception as e:
        print(f"Connected Graph: {e}")


# ... Continue with other graph creation methods following a similar structure
# Create a disconnected graph
def run_disconnected_graph():
    try:
        disconnected_graph = nx.disjoint_union(nx.complete_graph(5), nx.complete_graph(5))
        draw_graph_with_title(disconnected_graph, 'Disconnected Graph', 'lightcyan')
    except Exception as e:
        print(f"Disconnected Graph: {e}")

def run_bipartite_graph():
    try:
        bipartite_graph = nx.complete_bipartite_graph(3, 5)
        draw_graph_with_title(bipartite_graph, 'Bipartite Graph', 'orange')  # Changed color to 'orange'
    except Exception as e:
        print(f"Bipartite Graph: {e}")

def run_simple_graph():
    try:
        simple_edges = [(row['Source_Country'], row['Destination_Country']) for _, row in data.head(5).iterrows()]
        simple_graph = nx.Graph(simple_edges)
        draw_graph_with_title(simple_graph, 'Simple Graph', 'lightgreen')
    except Exception as e:
        print(f"Simple Graph: {e}")

def run_weighted_graph():
    try:
        if 'Capacity' in data.columns and pd.to_numeric(data['Capacity'], errors='coerce').notnull().all():
            data['Capacity'] = pd.to_numeric(data['Capacity'], errors='coerce')

            weighted_edges = [
                (row['Source_Country'], row['Destination_Country'], row['Capacity']) for _, row in data.iterrows()
            ]
            weighted_graph = nx.Graph()
            weighted_graph.add_weighted_edges_from(weighted_edges)

            draw_graph_with_title(weighted_graph, 'Weighted Graph', 'lightblue')
        else:
            raise ValueError("Column 'Capacity' either not found or contains non-numeric values.")
    except Exception as e:
        print(f"Weighted Graph: {e}")

def run_unweighted_graph():
    try:
        unweighted_edges = [(row['Source_Country'], row['Destination_Country']) for _, row in data.head(5).iterrows()]
        unweighted_graph = nx.Graph(unweighted_edges)
        draw_graph_with_title(unweighted_graph, 'Unweighted Graph', 'lightgreen')
    except Exception as e:
        print(f"Unweighted Graph: {e}")

def run_cyclic_graph():
    try:
        cyclic_graph = nx.cycle_graph(5)
        draw_graph_with_title(cyclic_graph, 'Cyclic Graph', 'lightcoral')
    except Exception as e:
        print(f"Cyclic Graph: {e}")

def run_multigraph():
    try:
        multigraph = nx.MultiGraph()
        multigraph.add_edges_from([(1, 2), (1, 2), (1, 2), (2, 3), (3, 4)])
        draw_graph_with_title(multigraph, 'Multigraph', 'lightyellow')
    except Exception as e:
        print(f"Multigraph: {e}")

def run_directed_acyclic_graph():
    try:
        dag = nx.random_tree(10, seed=42)
        draw_graph_with_title(dag, 'Directed Acyclic Graph', 'lightpink')
    except Exception as e:
        print(f"DAG: {e}")



def run_line_graph():
    try:
        line_graph = nx.line_graph(nx.complete_graph(5))
        draw_graph_with_title(line_graph, 'Line Graph', 'lightcyan')
    except Exception as e:
        print(f"Line Graph: {e}")


root = tk.Tk()
root.title("Graph Visualizer")
root.configure(bg='#6417FF')
buttons = [
    ("Directed Graph", run_directed_graph), ("Undirected Graph", run_undirected_graph),
    ("Pseudo Graph", run_pseudo_graph), ("Random Graph", run_random_graph),
    ("Complete Graph", run_complete_graph), ("Connected Graph", run_connected_graph),
    ("Disconnected Graph", run_disconnected_graph), ("Bipartite Graph", run_bipartite_graph),
    ("Simple Graph", run_simple_graph), ("Weighted Graph", run_weighted_graph),
    ("Unweighted Graph", run_unweighted_graph), ("Cyclic Graph", run_cyclic_graph),
    ("Multigraph", run_multigraph), ("Directed Acyclic Graph", run_directed_acyclic_graph),
    ("Line Graph", run_line_graph)
    # Add more buttons as needed
]

# Packing buttons with specified configurations
for text, func in buttons:
    button = tk.Button(root, text=text, command=func)
    button.configure(bg='white')  # Button background color
    button.pack(pady=10)  # Adjust the padding between buttons

root.mainloop()