


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value




class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # ma = None

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root,"")
        if traversal_type == "inorder":
            return self.inorder(tree.root,"")
        if traversal_type == "postorder":
            return self.postorder(tree.root,"")




    def preorder(self,start,traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right,traversal)
        return traversal

    def inorder(self,start,traversal):
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right,traversal)
        return traversal
    
    def postorder(self,start,traversal):
        if start:
            traversal = self.postorder(start.left,traversal)
            traversal = self.postorder(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal
             
    def levelorder(self,root):
        if root is None:
            return 
        queue = []
        nums = []
        queue.append(root)
        
        while len(queue) > 0:
            nums.append(queue[0].value)
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
        return nums

    def LeftView(self,root):
    
    # code here
        if not root:
            return
        q = []
        nums = []
        q.append(root)
        traversal = ""
        while len(q) > 0:
            n = len(q)
            
            for i in range(1,n+1):
                temp = q[0]
                q.pop(0)
                
                if i == 1:
                    nums.append(temp.value)
                
                if temp.right:
                    q.append(temp.right)
                    
                if temp.left:
                    q.append(temp.left)
        return nums

    # def function(self,root):
    #     if root is None:
    #         return 0
    #     x = self.func(root.left)
    #     y = self.func(root.right)
    #     ma = max(ma,x+y+1)
    #     return max((x,y)+1)

    # def diameter(self,root):
    #     ma = -10**8
    #     x = self.func(root)
    #     return ma






























tree = BinaryTree(1)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.levelorder(tree.root))
# print(tree.root.value)
# print(tree.diameter(tree.root))
print(tree.LeftView(tree.root))
