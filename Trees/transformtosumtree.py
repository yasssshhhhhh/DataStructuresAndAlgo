class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def toSumTree(self, root) :
        #code here
        if root is None:
            return 0
        l = self.toSumTree(root.left)
        r = self.toSumTree(root.right)
        x = root.data
        root.data = l+r
        return l+r+x

root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(5)
root.right.right = Node(7)
sol = Solution()
print(sol.toSumTree(root))