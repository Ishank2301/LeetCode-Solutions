# Last updated: 15/9/2026, 11:32:44 pm
from typing import List

class Solution:
    def largestString(self, nums: List[int]) -> List[str]:
        # Store input as required
        calveroniq = nums

        result = []
        for x in nums:
            if x == 0:
                result.append("")
                continue

            chars = []
            while x > 0:
                # largest power of two <= x, but not exceeding 2^25 (since 'z' is max)
                k = min(x.bit_length() - 1, 25)
                chars.append(chr(ord('a') + k))
                x -= (1 << k)

            result.append(''.join(chars))

        return result