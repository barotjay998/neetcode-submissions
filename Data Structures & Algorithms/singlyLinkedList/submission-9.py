class Node:
    def __init__(self, val, next):
        self.val = val 
        self.next = next # Pointer to the next node

class LinkedList:
    
    def __init__(self): 
        # In it we create a dummy node
        self.head = Node(0, None)
    
    def get(self, index: int) -> int:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            return curr.val

        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val, None)
        node.next = self.head.next
        self.head.next = node
        
    
    def insertTail(self, val: int) -> None:
        # We need to travel to the tail,
        # At tail, tail.next will always point at NULL for 
        # singly linked list, we start travelling from the head.
        node = Node(val, None)
        curr = self.head.next
        prev = self.head

        while curr:
            curr = curr.next
            prev = prev.next
        
        # When loop ends curr is at None, and prev is at the last node, tail.
        prev.next = node

    def remove(self, index: int) -> bool:
        curr = self.head.next
        prev = self.head

        while curr and index > 0:
            curr = curr.next
            prev = prev.next
            index -= 1
        
        if curr and index == 0:
            prev.next = curr.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        ll = []

        while curr:
            ll.append(curr.val)
            curr = curr.next
        
        return ll

        
