# Last updated: 15/9/2026, 11:33:44 pm
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        over = 0
        freq = {}
        l = 0
        for r in range(len(nums)):
            if freq.get(nums[r], 0) == k:
                over += 1
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            if over > 0:
                freq[nums[l]] -= 1
                if freq[nums[l]] == k:
                    over -= 1
                l += 1
        return len(nums) - l