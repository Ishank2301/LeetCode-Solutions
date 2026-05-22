class Solution:
    def isValid(self, s: str) -> bool:
        # Let's try it by paranthesis mapping
        mapping = {")": "(", "}": "{", "]": "["}

        stack = []
        # Check for parantheses in string:s
        for char in s:
            #Check if parathensis is in mapping hash map:
            if char in mapping:
    # Pop the top element if stack is not empty, otherwise assign a dummy value.
                top_ele = stack.pop() if stack else '#'
                if mapping[char]!= top_ele:
                    return False
            else:
                stack.append(char)
        return not stack       

                