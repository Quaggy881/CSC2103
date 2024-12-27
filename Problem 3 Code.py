import matplotlib.pyplot as plt
import time

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Add edges to the adjacency list
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graphs

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        traversal_order = []

        while queue:
            current = queue.pop(0)
            traversal_order.append(current)
            self.visualize_graph(current, visited)
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        self.visualize_graph(None, visited, final=True)
        return traversal_order

    def dfs(self, start_node):
        visited = set()
        traversal_order = []

        def dfs_recursive(node):
            visited.add(node)
            traversal_order.append(node)
            self.visualize_graph(node, visited)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        self.visualize_graph(None, visited, final=True)
        return traversal_order

    def visualize_graph(self, current_node, visited, final=False):
        plt.clf()
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                plt.plot([ord(node), ord(neighbor)], [1, 1], 'k-', zorder=1)
            color = 'green' if node in visited else 'blue'
            if node == current_node and not final:
                color = 'red'
            plt.scatter([ord(node)], [1], color=color, s=200, zorder=2)
            plt.text(ord(node), 1.1, node, fontsize=12, ha='center')
        plt.title("Graph Traversal" if not final else "Traversal Complete")
        plt.pause(1)

# Main program
if __name__ == "__main__":
    graph = Graph()

    print("Enter edges (format: node1 node2). Type 'done' to finish:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        u, v = edge.split()
        graph.add_edge(u, v)

    # Ensure the start node exists in the graph
    while True:
        start_node = input("Enter the start node: ")
        if start_node in graph.graph:
            break
        else:
            print("Start node not found in the graph! Please enter a valid node.")

    # Ensure the traversal method is valid
    while True:
        method = input("Choose traversal method (BFS/DFS): ").lower()
        if method in ['bfs', 'dfs']:
            break
        else:
            print("Invalid method! Please enter 'BFS' or 'DFS'.")

    plt.ion()
    if method == "bfs":
        order = graph.bfs(start_node)
        print("BFS Traversal Order:", order)
    elif method == "dfs":
        order = graph.dfs(start_node)
        print("DFS Traversal Order:", order)
    else:
        print("Invalid method selected!")
    plt.ioff()
    plt.show()