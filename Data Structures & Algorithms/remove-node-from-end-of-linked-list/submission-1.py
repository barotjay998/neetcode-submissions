# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # My solution: T: O(L), L is the length of linked list.
        # # Intuition: If I precompute the length of the linked list first, 
        # # then I can calculate what is the target index to be removed traversing forward
        # # in the linked list. If length=4, n=2, then target_idx = 4-2 = 2 (0 index LL).
        # # As usual, for linked list problems we will use dummy nodes to get 
        # # rid of edge cases.

        # dummy = ListNode
        # dummy.next = head

        # curr = dummy
        # length = 0
        # while curr.next != None:
        #     curr = curr.next
        #     length += 1
        
        # prev, curr = dummy, dummy.next
        # target_idx = length - n

        # while target_idx > 0 and curr.next:
        #     target_idx -= 1
        #     prev = curr
        #     curr = curr.next
        
        # prev.next = curr.next
        
        # return dummy.next


        # NeetCode solution: T: O(L)
        # Intuition, we need to remove the node that is at a distance N from the end 
        # of the LinkedList, we start two pointers L & R separated at a distance n,
        # and move them together till R reaches end of linked list, and L will be pointing 
        # to our target index. 
        dummy = ListNode(0, head)
        L = dummy
        R = head

        # separate L, R with a distance of n
        # we do not need to check for R.next since n will always be in bounds
        # as per constraints.
        while n > 0:
            n -= 1
            R = R.next

        while R:
            L = L.next
            R = R.next
        
        L.next = L.next.next
        
        return dummy.next



