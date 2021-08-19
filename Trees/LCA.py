class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def LCA(self,root,n1,n2):
        if root is None:
            return None
        if root.data == n1 or root.data == n2:
            return root

        l = self.LCA(root.left,n1,n2)
        r = self.LCA(root.right,n1,n2)
        if l and r :
            return root.data
        if l:
            return l
        else:
            return r

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(6)
sol = solution()
print(sol.LCA(root,4,3))
