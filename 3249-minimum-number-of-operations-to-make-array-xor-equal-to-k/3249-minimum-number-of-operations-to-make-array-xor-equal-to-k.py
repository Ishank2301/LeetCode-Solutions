class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        current_xor = 0
        
        # Step 1: Find the total XOR sum of the array
        for num in nums:
            current_xor ^= num
            
        # Step 2 & 3: XOR with k to find differing bits, then count them
        return (current_xor ^ k).bit_count()
