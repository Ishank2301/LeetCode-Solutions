# Last updated: 15/9/2026, 11:36:33 pm
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # oh, a easy after many days
        seen  = set() # Sets are specifically optimized for these duplicates checking condition
        for num in nums:
            if num in seen:
                return True  
            seen.add(num)  # Hilarious My friend asked me to use append haahahha
        return False