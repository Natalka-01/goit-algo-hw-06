def print_table(distances, visited):
    # Table header
    print("{:<15} {:<10} {:<10}".format("Station", "Distance", "Visited"))
    print("-" * 35)
    
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Yes" if vertex in visited else "No"
        print("{:<15} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Show table after each step
        print_table(distances, visited)

    return distances

# === Metro graph as a dictionary ===
metro_graph = {
    'Tsentralna': {'Ploshcha Rynok': 6, 'Vokzal': 6, 'Muzeina': 8},
    'Ploshcha Rynok': {'Tsentralna': 6, 'Universytet': 4},
    'Universytet': {'Ploshcha Rynok': 4, 'Zavodska': 5},
    'Zavodska': {'Universytet': 5},
    'Vokzal': {'Tsentralna': 6, 'Park': 4},
    'Park': {'Vokzal': 4, 'Muzeina': 3},
    'Muzeina': {'Park': 3, 'Tsentralna': 8}
}

# === Run Dijkstra from a chosen station ===
dijkstra(metro_graph, 'Park')
