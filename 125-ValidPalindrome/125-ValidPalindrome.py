# Last updated: 15/9/2026, 11:36:49 pm
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. First, build the clean string (alphanumeric only)
        # We also convert to lowercase so 'A' == 'a'
        result = ""
        for char in s:
            code = ord(char)
            # Check if it's a number (48-57), Uppercase (65-90), or Lowercase (97-122)
            if (48 <= code <= 57) or (65 <= code <= 90) or (97 <= code <= 122):
                # Manual lowercase conversion: if Uppercase, add 32 to get Lowercase
                if 65 <= code <= 90:
                    result += chr(code + 32)
                else:
                    result += char

        # 2. Use two pointers to check if the result is a palindrome
        n = len(result)
        i, j = 0, n - 1
        
        while i < j:
            if result[i] != result[j]:
                return False  # Found a mismatch, not a palindrome
            i += 1
            j -= 1
            
        return True  # If the loop finishes without returning False, it's a palindrome
