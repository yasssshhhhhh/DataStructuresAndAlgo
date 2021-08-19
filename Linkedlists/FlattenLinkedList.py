class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.bottom = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
            
            
        else:
            
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            new_node.next = None
            cur.next = new_node
            

    def flatten(root):
        #Your code here
        if root is None or root.next is None:
            return root
        root.next = flatten(root.next)
        root = merge(root,root.next)
        return root
        
    def merge(a,b):
        if a == None:
            return b
        if b == None:
            return a
        
        curr = Node(-1)
        res = curr
            
        while a is not None and b is not None:
            if a.data <= b.data:
                curr.bottom = a
                cur = cur.bottom
                a = a.bottom
            else:
                curr.bottom = b
                curr = curr.bottom
                b = b.bottom
        if a is None:
            curr.bottom = b
        else:
            curr.bottom = a
        return res.bottom