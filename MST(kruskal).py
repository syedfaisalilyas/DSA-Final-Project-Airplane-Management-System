import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()
data = data.dropna(subset=['Source_Country', 'Destination_Country'])


# Function to implement Kruskal's algorithm
def find(parent, i):
    while parent[i] != i:
        print(f"i: {i}, parent[i]: {parent[i]}")
        i = parent[i]
    return i

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
    print(f"parent: {parent}")


def kruskal(data):
    nodes = list(set(data['Source_Country']).union(set(data['Destination_Country'])))
    num_nodes = len(nodes)
    edges = []

    for _, row in data.iterrows():
        edges.append((row['Source_Country'], row['Destination_Country'], row['Flight_Duaration_in_minutes']))
    print(f"Number of Nodes: {num_nodes}")
    print(f"Number of Edges: {len(edges)}")
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}
    mst = []

    for node in nodes:
        parent[node] = node
        rank[node] = 0

    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)
        print('s')
        if x != y:
            mst.append((u, v, weight))
            union(parent, rank, x, y)
            print('a')
            
    return mst

# Using Kruskal's algorithm to get MST edges
mst_edges = kruskal(data)

# Plotting the MST
plt.figure(figsize=(10, 8))
for edge in mst_edges:
    plt.plot([edge[0], edge[1]], [0, edge[2]], marker='o', linestyle='-', color='lightblue')

plt.title('Minimum Spanning Tree (MST)')
plt.xlabel('Nodes')
plt.ylabel('Edge Weight')
plt.grid(True)
plt.show()
