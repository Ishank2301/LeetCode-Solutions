# Last updated: 15/9/2026, 11:36:46 pm
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        s = " ".join(s)
        return s
