class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class solution:

    def height(self,root):

            if root is None:
                return 0
            l = self.height(root.left)
            r = self.height(root.right)
            if abs(l-r)>1:
                self.f = 0
            return 1 + max(l,r)
        
    def isBalanced(self,root):
        self.f = 1
        self.height(root)
        return self.f
        


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
# root.left.right = Node(3)
# root.left.left = Node(4)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.right.right.right = Node(7)
# root.right.right.right.right = Node(7)
sol = solution()
print(sol.isBalanced(root))
