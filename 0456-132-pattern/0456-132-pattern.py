from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Determines if there is a 132 pattern in the given list of integers.
        
        A 132 pattern is a subsequence of three indices i, j, k such that
        i < j < k and nums[i] < nums[k] < nums[j].
        
        Time Complexity: O(N) - Each element is pushed and popped from the stack at most once.
        Space Complexity: O(N) - In the worst case, the stack stores all elements of the array.
        """
        # If the array has fewer than 3 elements, a 132 pattern cannot exist.
        if len(nums) < 3:
            return False
        
        # nums_k represents the '2' in the '132' pattern (nums[i] < nums[k] < nums[j]).
        # We initialize it to -infinity and want to maximize its value.
        nums_k = float('-inf')
        
        # The stack stores candidates for the '3' (nums[j]), which is the peak.
        # It maintains a monotonic decreasing order from bottom to top.
        stack = []
        
        # Traverse the array backwards (from right to left)
        for i in range(len(nums) - 1, -1, -1):
            # If we find a number smaller than our current maximized nums_k, 
            # we have successfully found a '1' (nums[i]) that satisfies nums[i] < nums[k].
            # Since nums_k was paired with a larger nums[j] to its right, the pattern is complete.
            if nums[i] < nums_k:
                return True
            
            # If the current number is greater than the element at the top of the stack,
            # the current number is a valid peak candidate ('3'). 
            # We pop the smaller numbers from the stack to update nums_k ('2'), 
            # ensuring nums_k is as large as possible.
            while stack and nums[i] > stack[-1]:
                nums_k = stack.pop()
            
            # Push the current number onto the stack as a potential '3' for future elements.
            stack.append(nums[i])
            
        return False
