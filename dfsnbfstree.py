class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
    
        while len(queue)>0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    def DFS_inorder(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return results
def build_tree():
    tree = BinarySearchTree()
    nodes = input("Enter nodes separated by space: ").split()
    for node in nodes:
        tree.insert(int(node))
    return tree

my_tree = build_tree()
#print(f"The tree is{my_tree.values} ")
while True:
    print("\nChoose a search method:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Insert nodes in treee")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"BFS Traversal: {my_tree.BFS()}")
    elif choice == '2':
        print(f"DFS Traversal: {my_tree.DFS_inorder()}")
    elif choice == '3':
        new = int(input("Enter the value yo want to insert: "))
        my_tree.insert(new)
        print(f"Value {new} inserted into the tree.")
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")