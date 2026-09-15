# Last updated: 15/9/2026, 11:34:21 pm
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0

        for num in nums:
            count += freq[num - k]
            count += freq[num + k]
            freq[num] += 1

        return count
