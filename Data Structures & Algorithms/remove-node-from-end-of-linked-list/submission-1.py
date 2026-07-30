# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        node = head
        pos = self.length(head) - n
        while pos > 0:
            prev = node
            node = node.next
            pos -= 1
        
        if not node: prev.next = None

        if prev: prev.next = node.next if node else None
        else: head = head.next

        return head