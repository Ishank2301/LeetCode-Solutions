# Last updated: 15/9/2026, 11:37:07 pm
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        temp = head  # use a single pointer to traverse

        while temp and temp.next:
            if temp.val == temp.next.val:
                # Skip the next duplicate node
                temp.next = temp.next.next
            else:
                temp = temp.next  # move forward if no duplicate

        return head
