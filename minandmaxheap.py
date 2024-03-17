class Heap:
    def __init__(self):  
        self.heap = []
    def _heapify_insert(self, arr, n, i):
        parent = (i - 1) // 2
        if parent >= 0:
            if arr[i] > arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
                self._heapify_insert(arr, n, parent)

    def _heapify_delete(self, arr, n, i):
        largest = i 
        left = 2 * i + 1 
        right = 2 * i + 2 
        if (left < n and arr[left] > arr[largest]):
            largest = left
        if (right < n and arr[right] > arr[largest]):
            largest = right
        if (largest != i):
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify_delete(arr, n, largest)
 
    def insert_max_heap(self, value):
        if value in self.heap:
            print("Value already exists")
            return
        self.heap.append(value)
        n = len(self.heap)
        self._heapify_insert(self.heap, n, n-1)

    def delete_max_heap(self):
        if not self.heap:
            print("Heap is empty")
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        n = len(self.heap)
        self._heapify_delete(self.heap, n, 0)

class MinHeap:
    def __init__(self):
        self.heap = []

    def _min_heapify(self, arr, n, i):
        if i == 0:
            return  

        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            self._min_heapify(arr, n, parent)

    def insert_min_heap(self, value):
        if value in self.heap:
            print("Value already exists")
            return
        self.heap.append(value)
        n = len(self.heap)
        self._min_heapify(self.heap, n, n-1)


max_heap = Heap()

min_heap = MinHeap()

while True: 
    print("""Menu:
    1. Insert into Max Heap
    2. Delete from Max Heap
    3. Display Max Heap
    4. Display Min Heap
    5. Compare Max Heap with Min Heap
    6. Exit""")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter value to insert into Max Heap: "))
        max_heap.insert_max_heap(value)
        min_heap.insert_min_heap(value)
    elif choice == 2:
        max_heap.delete_max_heap()
    elif choice == 3:
        print(f"Max Heap: {max_heap.heap}")
    elif choice == 4:
        print(f"Min Heap: {min_heap.heap}")
    elif choice == 5:
        if len(max_heap.heap) != len(min_heap.heap):
            print("Heaps are of different sizes and cannot be compared.")
        else:
            dif = 0
            same = 0
            for i in range(len(max_heap.heap)):
                if max_heap.heap[i] != min_heap.heap[i]:
                    print(f"Element different at index {i}: Max Heap - {max_heap.heap[i]}, Min Heap - {min_heap.heap[i]}")
                    dif += 1
                else: 
                    same += 1
            print(f"Number of different elements: {dif} ")
            print(f"Number of same elements: {same}")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")