class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        begin = 0
        counts = collections.defaultdict(int)
        ans = 0
        for end, num in enumerate(nums):
            while counts[num] == k:
                counts[nums[begin]] -= 1
                begin += 1
            counts[num] += 1
            ans = max(ans, end - begin + 1)
        return ans