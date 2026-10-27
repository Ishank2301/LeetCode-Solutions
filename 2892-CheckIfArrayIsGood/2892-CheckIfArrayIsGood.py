# Last updated: 27/10/2026, 8:48:10 pm
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)

        if len(nums) != mx + 1:
            return False

        freq = Counter(nums)

        if freq[mx] != 2:
            return False

        for i in range(1, mx):
            if freq[i] != 1:
                return False

        return True