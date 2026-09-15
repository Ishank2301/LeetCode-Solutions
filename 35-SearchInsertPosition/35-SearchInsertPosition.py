# Last updated: 15/9/2026, 11:37:56 pm
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
        
            if nums[mid] == target:
                return mid  # Found it! Return the index
        
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
            
    # If not found, 'low' is the index where target should be inserted
        return low 
