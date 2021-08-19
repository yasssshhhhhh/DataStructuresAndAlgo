


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None


    def prepend(self,data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node


    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self,key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev =None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count+=1
            cur = cur.next
            if cur == self.head:
                break
        return count


    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        Prev = None
        cur = self.head
        count = 0
        mid = size//2
        while cur and count < mid:
            count+=1
            Prev = cur
            cur = cur.next
        Prev.next = self.head

        split = CircularLinkedList()
        while cur.next != self.head:
            split.append(cur.data)
            cur = cur.next
        split.append(cur.data)


        self.print_list()
        print("\n")
        split.print_list()

    def remove_node(self,node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev =None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self,step):
        cur = self.head

        while len(self)>1:
            count = 1
            while count != step:
                cur = cur.next
                count+=1
            print("REMOVED: " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next






clist = CircularLinkedList()
clist.append("1")
clist.append("2")
clist.append("3")
clist.append("4")
# clist.split_list()
clist.josephus_circle(2)
# clist.remove("A")
# print(len(clist))
clist.print_list()