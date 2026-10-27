# Last updated: 27/10/2026, 8:48:40 pm
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        words = set(word1 + word2)
        for w in words:
            if abs(word1.count(w) - word2.count(w)) >3:
                return False
        return True
