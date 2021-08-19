


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def solve(self,root):
        if root is None:
           return 0
        l = self.solve(root.left)
        r = self.solve(root.right)
        
        self.ma = max (self.ma,l + r + root.data)
        # print(self.ma)
        return l + r + root.data
    def SubTree(self,root):
        self.ma = -9999
        self.solve(root)
        
        return self.ma










sol = solution()
root = node(-1)
root.left = node(-2)
root.right = node(3)
root.left.left = node(5)
root.left.right = node(5)
root.right.left = node(-6)
root.right.right = node(2)

print(sol.SubTree(root))
# print(sol.sumOfLongRootToLeafPath(root))