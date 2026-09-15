# Last updated: 15/9/2026, 11:37:13 pm
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits)))
        num += 1
        return [int (d) for d in str(num)]