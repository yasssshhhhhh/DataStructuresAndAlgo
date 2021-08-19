def removeLoop(self, head):
    
        low = head 
        high = head
        while low and high and high.next:
            low = low.next
            high = high.next.next
            if low == high:
                break
        if low == head:
            while high.next is not low:
                high = high.next
            high.next = None
        elif low == high:
            low = head
            while low.next != high.next:
                low = low.next
                high = high.next
            high.next = None