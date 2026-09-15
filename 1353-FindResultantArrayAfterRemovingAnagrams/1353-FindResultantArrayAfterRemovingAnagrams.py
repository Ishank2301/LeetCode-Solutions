# Last updated: 15/9/2026, 11:34:55 pm
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Always include the first word
        result = [words[0]]
        
        # Start comparing from the second word (index 1)
        for i in range(1, len(words)):
            # If the current word is NOT an anagram of the PREVIOUS word in the ORIGINAL list
            # Note: We compare with words[i-1], not result[-1]
            if sorted(words[i]) != sorted(words[i-1]):
                result.append(words[i])
                
        return result
