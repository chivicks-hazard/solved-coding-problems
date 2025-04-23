vertexData = ["A", "B", "C", "D"]

adjacency_matrix = [
    [0, 1, 1, 1], # A
    [1, 0, 1, 0], # B
    [1, 1, 0, 0], # C
    [1, 0, 0, 0]  # D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix: ")
    for row in matrix:
        print(row)
        
# print("vertexData:", vertexData)
# print_adjacency_matrix(adjacency_matrix)

def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()
        
        
# Using classes
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)] # Change 0 to None for directed and weighted graphs
        self.size = size
        self.vertex_data = [''] * size
        
    def add_edge(self, u, v): # Add weight for directed and weighted graphs
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1 # Change 1 to weight for directed and weighted graphs
            # self.adj_matrix[v][u] = 1 # Remove this line for directed and weighted graphs
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
            
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data, in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=" ")
        
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)
                
    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
        
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=" ")
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            
            
g = Graph(7)
g.add_vertex_data(0, "A")
g.add_vertex_data(1, "B")
g.add_vertex_data(2, "C")
g.add_vertex_data(3, "D")
g.add_vertex_data(4, "E")
g.add_vertex_data(5, "F")
g.add_vertex_data(6, "G")

# For unweighted graphs
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(1, 2)

# For directed and weighted graphs
# g.add_edge(0, 1, 3)
# g.add_edge(0, 2, 2)
# g.add_edge(3, 0, 2)
# g.add_edge(2, 1, 1)

# For undiirected graphs
# g.add_edge(3, 0)  # D - A
# g.add_edge(0, 2)  # A - C
# g.add_edge(0, 3)  # A - D
# g.add_edge(0, 4)  # A - E
# g.add_edge(4, 2)  # E - C
# g.add_edge(2, 5)  # C - F
# g.add_edge(2, 1)  # C - B
# g.add_edge(2, 6)  # C - G
# g.add_edge(1, 5)  # B - F

# For directed graphs
g.add_edge(3, 0)  # D -> A
g.add_edge(3, 4)  # D -> E
g.add_edge(4, 0)  # E -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 5)  # C -> F
g.add_edge(2, 6)  # C -> G
g.add_edge(5, 1)  # F -> B
g.add_edge(1, 2)  # B -> C

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs("D")

print("\nBreadth First Search starting from vertex D:")
g.bfs("D")