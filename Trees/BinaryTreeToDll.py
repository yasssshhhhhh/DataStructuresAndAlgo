
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None


# class BtoDll:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def convert(self, root):
#         if root is None:
#             return

#         self.convert(root.left)
        
#         # Now convert this node
#         node = root
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.right = node
#             node.left = self.tail
#         self.tail = node
        
#         # Finally convert right subtree
#         self.convert(root.right)
#         return self.head


# def BinaryTree2DoubleLinkedList(root):
 
#     converter = BtoDll()
#     return converter.convert(root)


# def print_dll(head):
#     while head is not None:
#         print(head.data, end=" ")
#         head = head.right



# if __name__ == "__main__":
  

#     root = Node(10)
#     root.left = Node(12)
#     root.right = Node(15)
#     root.left.left = Node(25)
#     root.left.right = Node(30)
#     root.right.left = Node(36)
    
#     # convert to DLL
#     head = BinaryTree2DoubleLinkedList(root)
#     print_dll(head)
    


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class BtoDll:
    # def __init__(self):
    #     self.head = None
    #     self.tail = None

    def convert(self, root):
        if root is None:
            return

        self.convert(root.left)
        
        # Now convert this node
        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node
        
        # Finally convert right subtree
        self.convert(root.right)
        return self.head


def BinaryTree2DoubleLinkedList(root):
 
    converter = BtoDll()
    return converter.convert(root)


def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.right



if __name__ == "__main__":
  

    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    # convert to DLL
    head = BinaryTree2DoubleLinkedList(root)
    print_dll(head)
    