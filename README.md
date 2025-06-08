# goit-algo-hw-06
goit-algo-hw-06
#  Metro Network Graph

This project models a small metro network using Python and the `networkx` library.

## Stations in the Network

- Tsentralna  
- Ploshcha Rynok  
- Universytet  
- Zavodska  
- Vokzal  
- Park  
- Muzeina

Each connection (edge) shows travel time in minutes.

## Graph Characteristics

- Number of stations (nodes): **7**
- Number of connections (edges): **7**
- The graph is connected: Yes

## Task 2: Comparing DFS and BFS (from Park to Zavodska)

In this task, we found a path between the **Park** and **Zavodska** stations using two algorithms:

### Results:

- **DFS (Depth-First Search):**  
  Park → Vokzal → Tsentralna → Ploshcha Rynok → Universytet → Zavodska

- **BFS (Breadth-First Search):**  
  Park → Vokzal → Tsentralna → Ploshcha Rynok → Universytet → Zavodska

### Conclusion:

- Both algorithms returned the same path because there is only one logical route in this case.
- **BFS** always finds the **shortest path** (by number of stations).
- **DFS** explores deeper paths first and may not return the shortest one.

### Key differences:

| Algorithm | How it works | Advantages |
|----------|----------------|-------------|
| DFS      | Goes as deep as possible before backtracking | Good for exploring the whole graph |
| BFS      | Explores level by level (all neighbors first) | Always finds the shortest path |