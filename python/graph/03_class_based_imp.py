




class Graph:
    def __init__(self, directed=False):
        self.graph = {} # adj list
        self.directed = directed


    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

        if not self.directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u,v):
        if u in self.graph:
            self.graph[u] = [(node, w) for node, w in self.graph[u] if node != v]

        if not self.directed and v in self.graph:
            self.graph[v] = [(node, w) for node, w in self.graph[v] if node != u]
        

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]

        for u in self.graph:
            self.graph[u] = [(v,w) for v,w in self.graph[u] if v != node]

    def to_adjacency_matrix(self):
        nodes = sorted(self.graph.keys())
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0] * size for _ in range(size)]

        for u in self.graph:
            for v, w in self.graph[u]:
                i, j = index[u], index[v]
                matrix[i][j] = w
        return nodes, matrix


    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Create a weighted undirected graph
g = Graph(directed=False)
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 1)
g.remove_edge('A', 'B')
g.remove_node('D')

g.print_graph()

nodes, matrix = g.to_adjacency_matrix()
print("Adjacency Matrix:")
print("   " + " ".join(nodes))
for i, row in enumerate(matrix):
    print(f"{nodes[i]}: {row}")