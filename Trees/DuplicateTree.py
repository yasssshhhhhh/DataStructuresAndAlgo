from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def solve(self,root):
        if root is None:
            return "$"
        self.s = ""
        if root.left is None and root.right is None:
            self.s = str(root.data)
            return self.s

        self.s = self.s + str(root.data)
        self.s = self.s + self.solve(root.left)
        self.s = self.s + self.solve(root.right)
        self.dict1[self.s] += 1
        return self.s


    def dupTree(self,root):
        self.dict1 = defaultdict(int)
        
        self.solve(root)
        for key,value in self.dict1.items():
            if value >= 2:
                return True
        return False



























root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)
root.right.right = Node(2)
root.right.right.left = Node(4)
root.right.right.right = Node(5)
sol = solution()
print(sol.dupTree(root))