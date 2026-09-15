# Last updated: 15/9/2026, 11:37:25 pm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        s = 0
        for i in nums:
            s+=i
            if s>maxsum:
                maxsum = s
            if s<0:
                s=0
        return maxsum

              