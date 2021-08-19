class node:
    f = 1
    s = 2
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def solve(self,root):
        # print(f)
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        
        l = self.solve(root.left)
        r = self.solve(root.right)
        if l+r != root.data:
            root.f =0
        return l + r + root.data

    def isSumtree(self,root):
        self.solve(root)
        return root.f

    # def print_f(self):
    #     f = 1
    #     self.changed_f(f)

    # def changed_f(self,f):
        
    #     print(f)















sol = solution()
root = node(60)
root.left = node(20)
root.right = node(30)
root.left.left = node(10)
root.left.right = node(5)
print(sol.isSumtree(root))
# sol.print_f()