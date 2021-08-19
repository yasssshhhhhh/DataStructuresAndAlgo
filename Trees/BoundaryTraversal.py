
class Node:

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class solution:
    def leftree(self,root,nums):
        if root is None:
            return
        if root.left:
            nums.append(root.data)
            self.leftree(root.left,nums)
        elif root.right:
            nums.append(root.data)
            self.leftree(root.right,nums)
            
    def leaf(self,root,nums):
        if root is None:
            return
        self.leaf(root.left,nums)
        if root.left is None and root.right is None:
            nums.append(root.data)
        self.leaf(root.right,nums)
        
    def rightree(self,root,nums):
        if root is None:
            return
        if root.right:
            self.rightree(root.right,nums)
            nums.append(root.data)
        elif root.left:
            self.rightree(root.left,nums)
            nums.append(root.data)

    def printBoundaryView(self, root):
        nums = []
        nums.append(root.data)
        self.leftree(root.left,nums)
        self.leaf(root,nums)
        self.rightree(root.right,nums)
        print(nums)
        return nums


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
sol = solution()
sol.printBoundaryView(root)
