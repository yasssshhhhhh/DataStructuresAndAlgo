# class node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class solution:
#     def solve(self,root,level):
#         if root is None:
#             return 
#         if root.left is None and root.right is None:
#             if self.leaflevel == 0:
#                self.leaflevel = level
#                return
#             return
#         self.solve(root.left,level+1)
#         self.solve(root.right,level+1)


#     def check(self,root):
#         level = 0
#         self.leaflevel = 0
        
#         self.solve(root,level) 
#         return self.ans




# root = node(1)
# root.left = node(2)
# root.right = node(3)
# root.left.left = node(4)
# root.left.right = node(5)
# sol = solution()
# print(sol.check(root))



class Node:
	
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class solution:

    def checkUtil(self,root, level):
        
        if root is None:
            return True

        if root.left is None and root.right is None:
    
            if self.leafLevel == 0 :
                self.leafLevel = level 
                return True

            return level == self.leafLevel

        return (self.checkUtil(root.left, level+1) and self.checkUtil(root.right, level+1))

    def check(self,root):
        self.level = 0
        self.leafLevel = 0
        return (self.checkUtil(root, self.level))


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(50)
root.left.left = Node(40)

# root.left.left = Node(3)
# root.left.right = Node(9)
# root.left.left.left = Node(1)
# root.left.right.left = Node(2)
sol = solution()
if(sol.check(root)):
	print("Leaves are at same level")
else:
	print("Leaves are not at same level")


