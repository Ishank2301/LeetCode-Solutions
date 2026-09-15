# Last updated: 15/9/2026, 11:36:35 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev
