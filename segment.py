class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self._update(2 * node + 1, start, mid, index, value)
            else:
                self._update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return (self._query(2 * node + 1, start, mid, left, right) +
                self._query(2 * node + 2, mid + 1, end, left, right))


if __name__ == "__main__":
    
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    
   
    seg_tree = SegmentTree(arr)
    
    while True:
        print("\nOperations:")
        print("1. Update a value")
        print("2. Query a range")
        print("3. Exit")
        
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == 1:
            index = int(input("Enter the index to update: "))
            value = int(input("Enter the new value: "))
            seg_tree.update(index, value)
            print(f"Updated value at index {index} to {value}")
        
        elif choice == 2:
            left = int(input("Enter the left bound of the range: "))
            right = int(input("Enter the right bound of the range: "))
            result = seg_tree.query(left, right)
            print(f"Sum of range [{left}, {right}] is: {result}")
        
        elif choice == 3:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
