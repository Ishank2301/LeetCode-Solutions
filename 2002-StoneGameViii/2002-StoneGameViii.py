# Last updated: 15/9/2026, 11:34:40 pm
class Solution:
    def stoneGameVIII(self, A: List[int]) -> int:
        n = len(A)
        s = list(accumulate(A))

        @cache
        def maxDiff(i):
            if i == n - 1: return s[n - 1]
            return max(maxDiff(i + 1), s[i] - maxDiff(i + 1))

        return maxDiff(1)