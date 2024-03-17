class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

def BFS(my_graph,node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m , end= " ")
        for neighbour in my_graph.adj_list[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
visited = set()
def DFS(visited,my_graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in my_graph.adj_list[node]:
            DFS(visited, my_graph, neighbour)

my_graph = Graph()

    
while True:
    print("\nChoose an option:")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Print Graph")
    print("4. BFS Traversal")
    print("5. DFS Traversal")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        vertex = int(input("Enter vertex to add: "))
        if my_graph.add_vertex(vertex):
            print("Vertex added successfully.")
        else:
            print("Vertex already exists.")
    elif choice == '2':
        v1 = int(input("Enter first vertex of edge: "))
        v2 = int(input("Enter second vertex of edge: "))
        if my_graph.add_edge(v1, v2):
            print("Edge added successfully.")
        else:
            print("One or both vertices do not exist.")
    elif choice == '3':
        print("Graph:")
        my_graph.print_graph()
    elif choice == '4':
        start_node = int(input("Enter the starting node for BFS traversal: "))
        print("BFS Traversal:")
        BFS(my_graph, start_node)
    elif choice == '5':
        start_node = int(input("Enter the starting node for DFS traversal: "))
        print("DFS Traversal:")
        DFS(visited, my_graph, start_node)
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")