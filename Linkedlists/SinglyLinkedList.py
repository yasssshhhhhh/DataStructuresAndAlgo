
# from _typeshed import Self
# from typing import Counter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Previous node not in the list")
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
        cur_node = self.head

        if cur_node and cur_node ==key:
            self.head = cur_node.next
            cur_node = None
            return
        
        Prev = None
        while cur_node and cur_node.data!=key:
            Prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        Prev.next = cur_node.next
        cur_node = None


    def delete_at_pos(self,pos):
        cur_node = self.head

        if pos ==0:
            self.head = cur_node.next
            cur_node = None
            return

        Prev = None
        count =1
        while cur_node and count!=pos:
            Prev = cur_node
            cur_node = cur_node.next
            count+=1
        
        if cur_node is None:
            return
        
        Prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count+=1
            cur_node = cur_node.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def Node_swap(self,key1,key2):
        if key1 == key2:
            return
        
        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data!= key1:
            prev_1= cur_1
            cur_1 = cur_1.next

        
        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data!= key2:
            prev_2= cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return
        
        if prev_1:
            prev_1.next = cur_2
        else:
            self.head =  cur_2


        if prev_2:
            prev_2.next = cur_1

        else:
            self.head = cur_1

        cur_1.next,cur_2.next = cur_2.next,cur_1.next


    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_sortedLists(self,llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = q
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
        


    def Remove_duplicates(self):
        prev = None
        cur = self.head

        dict1 = {}
        while cur:
            if cur.data in dict1:
                prev.next = cur.next
                cur = None
            else:
                dict1[cur.data] = 1
                prev = cur
            cur = prev.next


    def Nth_to_last_Node(self,n):
        

        # Method-1
        # total_len = self.len_iterative()
        # cur = self.head
        # while cur:
        #     if total_len == n:
        #         print(cur.data)
        #         return 
        #     total_len-=1
        #     cur = cur.next
        # if not cur:
        #     return 

        # Method-2
        p = self.head
        q = self.head
        
        count = 0
        while q and count < n:
            q = q.next
            count+=1
        if not q:
            print("NOT present")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data


    def count_occurences(self,data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count +=1
            cur = cur.next
        return count

    def rotate(self,k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count<k:
            prev = p
            p = p.next
            q = q.next
            count+=1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def IsPalindrome(self):
        # Method-1
        s=""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]


    def tail_to_head(self):
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        cur.next= self.head
        prev.next = None
        self.head = cur


    def sum_two_list(self,llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i =p.data
            if not q:
                j = 0
            else:
                j = q.data
            
            s = i+j+carry
            if s>=10:
                carry = 1
                remainder = s%10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()

    def reverse_of_size(self):
        prev = None
        cur = self.head
        count = 0
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count+=1
        if nxt:
            self.head.next = self.reverse_of_size(nxt,k)
        return prev

    def segregate(self):
        #code here
        count = [0,0,0]
        ptr = self.head
        while ptr:
           count[ptr.data]+=1
           ptr = ptr.next
           
           
        i = 0
        ptr = self.head
        while ptr:
            if count[i] ==0:
                i+=1
            else:
                ptr.data = i
                count[i]-=1
                ptr = ptr.next
        return self.head



# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)
# llist1.merge_sortedLists(llist2)

llist = LinkedList()

# # llist.insert_after_node(llist.head.next,"F")
# # llist.delete_node("B")
# llist.Node_swap("B","E")

 
# llist = LinkedList()
# llist1.append(3)
# llist1.append(4)
# llist1.append(5)
# llist2.append(4)
# llist2.append(5)

# # llist.Nth_to_last_Node(2)

# # llist.tail_to_head()
# llist1.sum_two_list(llist2)

llist.append(2)
llist.append(0)
llist.append(2)
llist.append(1)
llist.append(1)
llist.append(0)
llist.segregate()
# sum.print_list()
llist.print_list(
    
)
