# Last updated: 15/9/2026, 11:36:11 pm
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        has_odd = False

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True

        if has_odd:
            length += 1

        return length
