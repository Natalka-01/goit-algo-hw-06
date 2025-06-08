import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# === Create the metro graph ===
G = nx.Graph()

stations = [
    "Tsentralna",
    "Ploshcha Rynok",
    "Universytet",
    "Zavodska",
    "Park",
    "Vokzal",
    "Muzeina"
]
G.add_nodes_from(stations)

edges = [
    ("Tsentralna", "Ploshcha Rynok", 6),
    ("Ploshcha Rynok", "Universytet", 4),
    ("Universytet", "Zavodska", 5),
    ("Tsentralna", "Vokzal", 6),
    ("Vokzal", "Park", 4),
    ("Park", "Muzeina", 3),
    ("Muzeina", "Tsentralna", 8)
]
G.add_weighted_edges_from(edges)

# === DFS (Depth-First Search) ===
def dfs_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path
    return None

# === BFS (Breadth-First Search) ===
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# === Start and goal stations ===
start = "Park"
end = "Zavodska"

# === Find paths ===
dfs_result = dfs_path(G, start, end)
bfs_result = bfs_path(G, start, end)

# === Print results ===
print("DFS path from Park to Zavodska:")
print(" → ".join(dfs_result))

print("\nBFS path from Park to Zavodska:")
print(" → ".join(bfs_result))

# === Visualize the graph ===
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d} min" for u, v, d in G.edges(data='weight')})
plt.title("Metro Station Network")
plt.show()