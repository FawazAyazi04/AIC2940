import heapq

class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
        self.total_cost = 0
        self.heuristic = 0  # Added heuristic attribute
        self.parent = None

    def __lt__(self, other):
        return self.heuristic < other.heuristic  # Compare based on heuristic value

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(start.total_cost, start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node.state == goal.state:
            path = []
            total_cost = current_node.total_cost
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], total_cost

        if current_node.state not in visited:
            visited.add(current_node.state)
            for neighbor, edge_cost in graph[current_node.state]:
                neighbor_node = Node(neighbor, edge_cost)
                neighbor_node.parent = current_node
                neighbor_node.total_cost = current_node.total_cost + edge_cost
                heapq.heappush(priority_queue, (neighbor_node.total_cost, neighbor_node))

def a_star_search(graph, start, goal):
    visited = set()
    priority_queue = [(start.total_cost + start.heuristic, start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node.state == goal.state:
            path = []
            total_cost = current_node.total_cost
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], total_cost

        if current_node.state not in visited:
            visited.add(current_node.state)
            for neighbor, edge_cost in graph[current_node.state]:
                neighbor_node = Node(neighbor, edge_cost)
                neighbor_node.parent = current_node
                neighbor_node.total_cost = current_node.total_cost + edge_cost
                neighbor_node.heuristic = heuristic(neighbor)  # Use node position as heuristic
                heapq.heappush(priority_queue, (neighbor_node.total_cost + neighbor_node.heuristic, neighbor_node))

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = [(start.heuristic, start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node.state == goal.state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], 0  # Total cost is not explicitly calculated in Best-First Search

        if current_node.state not in visited:
            visited.add(current_node.state)
            for neighbor, edge_cost in graph[current_node.state]:
                neighbor_node = Node(neighbor, edge_cost)
                neighbor_node.parent = current_node
                neighbor_node.heuristic = heuristic(neighbor)  # Use node position as heuristic
                heapq.heappush(priority_queue, (neighbor_node.heuristic, neighbor_node))

# Define a heuristic function
def heuristic(node):
    # Use the position of the node as the heuristic value
    # In this case, we assume that the heuristic is the distance from the goal node
    return ord('Z') - ord(node)

# Example graph (list of tuples)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 2), ('F', 5)],
    'C': [('F', 4), ('G', 8)],
    'D': [('G', 2)],
    'E': [('G', 3), ('A', 7)],
    'F': [('G', 1), ('A', 1)],
    'G': []
}

# User input for source and goal nodes
source = input("Enter the source node: ")
goal = input("Enter the goal node: ")

# Creating nodes for source and goal with actual cost
source_node = Node(source, 0)
goal_node = Node(goal, 0)

# Define a function to calculate the total cost of a path
def calculate_total_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        for neighbor, cost in graph[current_node]:
            if neighbor == next_node:
                total_cost += cost
                break
    return total_cost

# Running Uniform Cost Search, A* Search, and Best-First Search
path_ucs, total_cost_ucs = uniform_cost_search(graph, source_node, goal_node)
path_a_star, total_cost_a_star = a_star_search(graph, source_node, goal_node)
path_best_first, total_cost_best_first = best_first_search(graph, source_node, goal_node)

# Calculate the total cost for each path
total_cost_path_ucs = calculate_total_cost(graph, path_ucs)
total_cost_path_a_star = calculate_total_cost(graph, path_a_star)
total_cost_path_best_first = calculate_total_cost(graph, path_best_first)

# Printing the paths and total costs
print("Uniform Cost Search Path:", path_ucs)
print("Total Cost (Uniform Cost Search):", total_cost_ucs)
print("Total Cost (Path):", total_cost_path_ucs)
print("A* Search Path:", path_a_star)
print("Total Cost (A* Search):", total_cost_a_star)
print("Total Cost (Path):", total_cost_path_a_star)
print("Best-First Search Path:", path_best_first)
print("Total Cost (Best-First Search):", total_cost_best_first)
print("Total Cost (Path):", total_cost_path_best_first)
if total_cost_best_first>total_cost_a_star:
    print(f"The best searching technique for this path is best_first_search")
elif total_cost_best_first>total_cost_ucs:
    print(f"The best searching technique for this path is best_first_search")
elif total_cost_a_star>total_cost_ucs:
    print(f"The best searching technique for this path is a_star")
else:
    print(f"The best searching technique for this path is uniform_cost_search")
    