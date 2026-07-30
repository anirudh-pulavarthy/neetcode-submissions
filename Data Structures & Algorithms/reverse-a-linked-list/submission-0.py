# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            old = head.next     # preserve next
            head.next = prev    # set next to previous

            prev = head         # update previous
            head = old          # move to the next one

        return prev