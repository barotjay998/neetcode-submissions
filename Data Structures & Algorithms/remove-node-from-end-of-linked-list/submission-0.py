# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # precompute the length first then we can easily calculate
        # the exact index in forward direction.
        # use dummy head node.

        dummy = ListNode
        dummy.next = head

        curr = dummy
        length = 0
        while curr.next != None:
            curr = curr.next
            length += 1
        
        prev, curr = dummy, dummy.next
        target_idx = length - n

        while target_idx > 0 and curr.next:
            target_idx -= 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        
        return dummy.next

