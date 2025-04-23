class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)] # Change 0 to None for directed and weighted graphs
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)] # Union find array | Add this line for union-find cyclic detection
        
    def add_edge(self, u, v): # Add weight for directed and weighted graphs
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1 # Change 1 to weight for directed and weighted graphs
            self.adj_matrix[v][u] = 1 # Remove this line for directed and weighted graphs
    
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
            
    def dfs_util(self, v, visited, recStack): # Change parent to recStack for directed graphs
        visited[v] = True
        recStack[v] = True
        print("Current vertex:", self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack): # Change v to recStack for directed graphs
                        return True
                elif recStack[i]: # Change (parent != 1) to recStack for directed graphs
                    return True
                    
        recStack[v] = False
        return False
        
    # DFS Cyclic Detection
    # def is_cyclic(self):
        # visited = [False] * self.size
        # recStack = [False] * self.size # Add this line for directed graphs
        # for i in range(self.size):
            # if not visited[i]:
                # if self.dfs_util(i, visited, recStack): # Change -1 to recStack for directed graphs
                    # return True
        # return False
        
    # Union-Find Cyclic Detection
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
        
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print("Union:", self.vertex_data[x], "x", self.vertex_data[y])
        self.parent[x_root] = y_root
        print(self.parent, "\n")
        
    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_matrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    if x == y:
                        return True
                    self.union(x, y)
        return False
        

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

# For undirected graphs
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
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

# g.print_graph()
print("\nGraph has cycle:", g.is_cyclic())

    