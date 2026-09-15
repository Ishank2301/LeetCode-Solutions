# Last updated: 15/9/2026, 11:34:37 pm
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        chars = set(s)

        for i, ch in enumerate(s):
            if ch.lower() not in chars or ch.upper() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right

        return s
