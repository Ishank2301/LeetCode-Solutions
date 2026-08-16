class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        n = len(s)

        if n <= 1:
            return False

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False


        for ch in s:
            if ch in '([{':          # opening bracket
                stack.append(ch)
            else:                     # closing bracket
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
        
        return len(stack) == 0        # stack must be empty at the end

        #Is this exceptionally the best so far answer:













