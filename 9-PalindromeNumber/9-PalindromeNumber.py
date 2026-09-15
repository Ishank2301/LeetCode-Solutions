# Last updated: 15/9/2026, 11:38:35 pm
class Solution:  
    def isPalindrome(self, x: int) -> bool:  
        x = str(x)  
        return x == x[::-1]  