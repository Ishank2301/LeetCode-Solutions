# Last updated: 15/9/2026, 11:32:43 pm
from math import gcd
from typing import List

class Solution:
    def maxValidSplits(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Prefix and Suffix GCD arrays
        pre = [0] * n
        suf = [0] * n

        for i in range(n):
            pre[i] = gcd(pre[i-1], nums[i]) if i > 0 else nums[i]

        for i in range(n-1, -1, -1):
            suf[i] = gcd(suf[i+1], nums[i]) if i+1 < n else nums[i]

        # Count valid splits in the original array
        ans = sum(pre[i] == suf[i+1] for i in range(n-1))

        # Try removing each element
        for r in range(n):
            score = 0

            # Case 1: Split is strictly to the LEFT of the removed element (i < r-1)
            # We stop at r-2 to avoid the central split (handled in Case 2)
            right_tail = suf[r+1] if r+1 < n else 0
            g = 0  # GCD of nums[i+1 .. r-1]
            for i in range(r-2, -1, -1):
                g = gcd(nums[i+1], g)  # Now g = GCD(nums[i+1 .. r-1])
                if pre[i] == gcd(g, right_tail):
                    score += 1

            # Case 2: Split is at or after the removed element (i >= r)
            # This also exclusively handles the central split (i = r-1 / i = r overlap)
            left_head = pre[r-1] if r > 0 else 0
            g = 0  # GCD of nums[r+1 .. i]
            for i in range(r, n-1):
                # For i == r, g is 0 (empty segment). Correctly checks split between r-1 and r+1.
                if gcd(left_head, g) == suf[i+1]:
                    score += 1
                # Update g for the next iteration: add nums[i+1] to the left segment
                g = gcd(g, nums[i+1])

            ans = max(ans, score)

        return ans
            

            