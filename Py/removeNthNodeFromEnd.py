# LeetCode 19 - Remove Nth Node From End of List (Medium)
#
# Given the head of a linked list, remove the n-th node counting from the end of
# the list, then return the head of the modified list.
#
# n is always valid (1 <= n <= length of the list). Removing the only node leaves
# an empty list, and n may well point at the head itself, so the head you return
# may not be the head you were given.
#
# The follow-up asks you to do it in a single pass, which is what the two-pointer
# trick (start one pointer n nodes ahead, then advance both) is for.
#
# Example: 1->2->3->4->5 with n = 2  ->  1->2->3->5
#
# The code below is an unfinished attempt.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head

    i = 0

    while i < n:
        succ = curr
        curr = curr.next
        
    


print(removeNthFromEnd[[1,2,3,4], 2])
   


