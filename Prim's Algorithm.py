import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    def min_key(self, key, in_mst):
        min_value = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if not in_mst[v] and key[v] < min_value:
                min_value = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V  # Initialize all keys as infinite
        parent = [-1] * self.V       # Array to store the MST
        in_mst = [False] * self.V    # To track vertices included in MST
        
        key[0] = 0  # Start with the first vertex
        
        for _ in range(self.V):
            u = self.min_key(key, in_mst)  # Pick vertex with minimum key
            in_mst[u] = True              # Include it in MST
            
            for v in range(self.V):       # Update key values of adjacent vertices
                if self.graph[u][v] and not in_mst[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


# Example Usage
if __name__ == "__main__":
    vertices = 5
    g = Graph(vertices)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    print("Minimum Spanning Tree using Prim's Algorithm:")
    g.prim_mst()
