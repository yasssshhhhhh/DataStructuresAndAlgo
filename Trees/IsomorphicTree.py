class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def IsomorphicTree(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        a = (self.IsomorphicTree(root1.left,root2.left)
        and self.IsomorphicTree(root1.right,root2.right))
        b = (self.IsomorphicTree(root1.left,root2.right) 
        and self.IsomorphicTree(root1.right,root2.left))
        return a or b






root1 = node(1)
root1.left = node(2)
root1.right = node(3)
root1.left.left = node(4)



root2 = node(1)
root2.left = node(3)
root2.right = node(2)
root2.right.right = node(4)

sol = solution()
print(sol.IsomorphicTree(root1,root2))