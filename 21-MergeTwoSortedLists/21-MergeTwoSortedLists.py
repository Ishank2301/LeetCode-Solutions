# Last updated: 15/9/2026, 11:38:15 pm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)   # dummy node
        tmp1, tmp2, tmp3 = list1, list2, head

        while tmp1 is not None and tmp2 is not None:
            if tmp1.val <= tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
            tmp3 = tmp3.next   # always move tmp3 forward

        # Attach whichever list is not finished
        if tmp1 is not None:
            tmp3.next = tmp1
        else:
            tmp3.next = tmp2

        return head.next   # return the merged list (skip dummy node)
