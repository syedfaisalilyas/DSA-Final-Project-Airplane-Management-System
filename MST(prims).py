import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Function to implement Prim's algorithm
def prim(data):
    nodes = list(set(data['Source_Country']).union(set(data['Destination_Country'])))
    num_nodes = len(nodes)
    I = float('inf')
    cost = [[I] * num_nodes for _ in range(num_nodes)]

    node_to_index = {node: i for i, node in enumerate(nodes)}
    for _, row in data.iterrows():
        source = row['Source_Country']
        dest = row['Destination_Country']
        cost[node_to_index[source]][node_to_index[dest]] = row['Flight_Duaration_in_minutes']
        cost[node_to_index[dest]][node_to_index[source]] = row['Flight_Duaration_in_minutes']

    mst = []
    selected = [False] * num_nodes
    selected[0] = True

    for _ in range(num_nodes - 1):
        min_val = I
        x = y = 0
        for i in range(num_nodes):
            if selected[i]:
                for j in range(num_nodes):
                    if not selected[j] and cost[i][j]:
                        if min_val > cost[i][j]:
                            min_val = cost[i][j]
                            x = i
                            y = j

        mst.append((nodes[x], nodes[y], min_val))
        selected[y] = True

    return mst

# Using Prim's algorithm to get MST edges
mst_edges = prim(data)

# Plotting the MST
plt.figure(figsize=(10, 8))
for edge in mst_edges:
    plt.plot([edge[0], edge[1]], [0, edge[2]], marker='o', linestyle='-', color='lightblue')

plt.title('Minimum Spanning Tree (MST)')
plt.xlabel('Nodes')
plt.ylabel('Edge Weight')
plt.grid(True)
plt.show()
plt.savefig('mst_plot.png')  # Save the plot as an image file
