class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class solution:
    def LCA(self,root,a,b):
        if root is None:
            return None
        if root.data == a or root.data == b:
            return root

        l = self.LCA(root.left,a,b)
        r = self.LCA(root.right,a,b)
        if l and r :
            return root
        if l:
            return l
        else:
            return r

    def solve(self,root,val):
        if root is None:
            return 0
        if root.data == val:
            return 1
        c = self.solve(root.left,val)
        d = self.solve(root.right,val)
        if not c and not d:
            return 0
        else:
            return c+d+1

    def finddist(self,root,a,b):
        lca = self.LCA(root,a,b)
        x = self.solve(lca,a)
        y = self.solve(lca,b)
        return x+y-2











root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

sol = solution()
print(sol.finddist(root,4,7))