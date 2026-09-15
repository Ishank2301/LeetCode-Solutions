# Last updated: 15/9/2026, 11:34:31 pm
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Initialize with the first element
        max_so_far = nums[0]
        current_sum = nums[0]
    
        for i in range(1, len(nums)):
            # Check if the subarray is still ascending
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                # Ascending order broken, reset current_sum
                current_sum = nums[i]
        
            # Update the overall maximum
            max_so_far = max(max_so_far, current_sum)
        
        return max_so_far
