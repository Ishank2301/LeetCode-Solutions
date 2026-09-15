# Last updated: 15/9/2026, 11:35:48 pm
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        counts = Counter(nums)
        degree = max(counts.values())

        first={}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        
        res = len(nums)
        for num in counts:
            if counts[num] == degree:
                res = min(res, last[num] - first[num] + 1)

        return res

        