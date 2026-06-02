class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums) - 1

        # Pass 1: move all 0s to the front
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
            i += 1

        # Pass 2: move all 2s to the back
        i = len(nums) - 1
        while i >= low:
            if nums[i] == 2:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
            i -= 1