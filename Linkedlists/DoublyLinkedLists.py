class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

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
            


    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_node_after(self,key,data):
        new_node = Node(data)
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next


    def add_node_before(self,key,data):
        new_node = Node(data)
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                prv = cur.prev
                prv.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prv

    def delete(self,key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # case 1
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                    # case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur =  None
                    self.head = nxt
                    return
            elif cur.data == key:
                # case 3
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev


    def delete_node(self,node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # case 1
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                    # case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur =  None
                    self.head = nxt
                    return
            elif cur == node:
                # case 3
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


    def remove_duplicates(self):
        cur = self.head
        dict1 = {}
        while cur:
            if cur.data not in dict1:
                dict1[cur.data] = 1
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_sum(self,sum_value):
        p = self.head
        q = None
        pairs = []
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_value:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs

    # def countpairs(first,second,value):
    #     count = 0

    #     while first and second and first!=second and second.next != first:

    #         if first.data + second.data == value:
    #             count+=1
    #             first = first.next
    #             second = second.prev

    #         elif first.data + second.data > value:
    #             second = second.prev
    #         else:
    #             first = first.next
    #     return count


    def count_triplets(self,x):
        if self.head == None:
            return 0
        count = 0  
        current = self.head
        first = None
        last = None

        last = self.head
        while last.next:
            last = last.next
        lasted = last
        while current:
            first = current.next
            last = lasted

            while first and last and first!= last and last.next != first:
                # print(first.data)
                # print(last.data)
                value = x-current.data
                if first.data + last.data ==  value:
                    count+=1
                    first = first.next
                    last = last.prev
                elif first.data + last.data > value:
                    last = last.prev
                else:
                    first = first.next

            current = current.next
        return count
    
dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(4)
dlist.append(5)
dlist.append(6)
dlist.append(8)
dlist.append(9)
# print(dlist.pairs_sum(5))
# dlist.prepend(6)
# dlist.add_node_after(2,11)
# dlist.reverse()
print(dlist.count_triplets(15))

# dlist.print_list()