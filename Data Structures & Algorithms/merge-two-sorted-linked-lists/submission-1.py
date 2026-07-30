# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        mergedList = ListNode()

        p1, p2, ans = list1, list2, mergedList
        while p1 or p2:

            if not p2:
                ans.val = p1.val
                p1 = p1.next

            elif not p1:
                ans.val = p2.val
                p2 = p2.next

            elif (p1.val <= p2.val):
                ans.val = p1.val
                p1 = p1.next
            
            else: #(p1.val > p2.val):
                ans.val = p2.val
                p2 = p2.next

            if p1 or p2: ans.next = ListNode()
            ans = ans.next

        return mergedList