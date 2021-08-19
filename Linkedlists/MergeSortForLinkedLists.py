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



    def mergeSort(self,head):
        if (head.next == None):
            return head
        
        mid = self.findMid(head)
        head2 = mid.next
        mid.next = None
        newHead1 = self.mergeSort(head)
        newHead2 = self.mergeSort(head2)
        finalHead = self.merge(newHead1, newHead2)
        return finalHead

# Function to merge two linked lists
    def merge(self,head1,head2):
        merged = Node(-1)
        
        temp = merged
        # While head1 is not null and head2
        # is not null
        while (head1 != None and head2 != None):
            if (head1.data < head2.data):
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        
        # While head1 is not null
        while (head1 != None):
            temp.next = head1
            head1 = head1.next
            temp = temp.next
        
        # While head2 is not null
        while (head2 != None):
            temp.next = head2
            head2 = head2.next
            temp = temp.next
        
        return merged.next

    # Find mid using The Tortoise and The Hare approach
    def findMid(self,head):
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow


llist = LinkedList()
llist.append(4)
llist.append(2)
llist.append(1)
llist.append(5)
llist.append(3)
llist.mergeSort(llist.head)
llist.print_list()