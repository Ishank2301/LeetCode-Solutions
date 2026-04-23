// Problem    : Longest Substring Without Repeating Characters
// Difficulty : Medium
// URL        : https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        ans = 0
        
        # j is the 'leading edge' of the window
        for j in range(len(s)):
            # If we see a duplicate, shrink the window from the left
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            # Add the current character and update the max length
            seen.add(s[j])
            ans = max(ans, j - i + 1)
            
        return ans
