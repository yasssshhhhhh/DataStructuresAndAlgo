# class node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class solution:

#     def solve(self,root):
#         if root is None:
#             return
#         self.value = 0
#         if root.left is None and root.right is None:
#             self.value += root.data
#             return self.value
#         self.value += root.data
#         self.value += self.solve(root.left)
#         if self.value > self.max:
#             self.max = self.value
#         self.value += self.solve(root.right)

#         return self.max

        
#     def sumOfLongRootToLeafPath(self,root):
#         self.max = -1
#         self.value = 0
#         val = self.solve(root)
#         return val



# sol = solution()
# root = node(4)
# root.left = node(2)
# root.right = node(5)
# root.left.left = node(7)
# root.left.right = node(1)
# root.right.left = node(2)
# root.right.right = node(3)
# root.left.right.left = node(6)

# print(sol.sumOfLongRootToLeafPath(root))







class getNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def SumOfLongRootToLeafPath(root, Sum, Len,
							maxLen, maxSum):
								
	# if true, then we have traversed a
	# root to leaf path
	if (not root):
		
		# update maximum Length and maximum Sum
		# according to the given conditions
		if (maxLen[0] < Len):
			maxLen[0] = Len
			maxSum[0] = Sum
		elif (maxLen[0]== Len and
			maxSum[0] < Sum):
			maxSum[0] = Sum
		return

	# recur for left subtree
	SumOfLongRootToLeafPath(root.left, Sum + root.data,
							Len + 1, maxLen, maxSum)

	# recur for right subtree
	SumOfLongRootToLeafPath(root.right, Sum + root.data,
							Len + 1, maxLen, maxSum)
    


def SumOfLongRootToLeafPathUtil(root):
	
	# if tree is NULL, then Sum is 0
	if (not root):
		return 0

	maxSum = [-999999999999]
	maxLen = [0]

	# finding the maximum Sum 'maxSum' for
	# the maximum Length root to leaf path
	SumOfLongRootToLeafPath(root, 0, 0,
							maxLen, maxSum)

	# required maximum Sum
	return maxSum[0]

if __name__ == '__main__':
	
	root = getNode(4)	
	root.left = getNode(2)	
	root.right = getNode(5)	  	
	root.left.left = getNode(7) 	
	root.left.right = getNode(1)
	root.right.left = getNode(2)		
	root.right.right = getNode(1)
	root.left.right.left = getNode(5)
root.left.right.right = getNode(6)

print("Sum = ", SumOfLongRootToLeafPathUtil(root))

