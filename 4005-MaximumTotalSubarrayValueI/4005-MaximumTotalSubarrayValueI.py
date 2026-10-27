# Last updated: 27/10/2026, 8:47:31 pm
class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        return k*max(A) - k*min(A)