# Last updated: 15/9/2026, 11:33:15 pm
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter

class Solution:
    def partitionArray(self, nums, k):
        size = len(nums)
        
        if size % k != 0:
            return False
        groups = size // k
        counts = Counter(nums)
        for freq in counts.values():
            if freq > groups:
                return False
        
        return True

        