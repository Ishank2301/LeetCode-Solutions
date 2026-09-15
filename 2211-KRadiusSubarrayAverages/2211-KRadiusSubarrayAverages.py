# Last updated: 15/9/2026, 11:34:16 pm
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        avgs = [-1] * n
        
        # If the array is smaller than the required window, return all -1
        if n < window_size:
            return avgs
        
        # 1. Calculate the sum of the first valid window (0 to 2k)
        current_window_sum = sum(nums[:window_size])
        
        # 2. The first center is at index k
        avgs[k] = current_window_sum // window_size
        
        # 3. Slide the window from the second possible center (k + 1)
        for i in range(k + 1, n - k):
            # The new element entering from the right is at index i + k
            # The old element leaving from the left is at index i - k - 1
            current_window_sum += nums[i + k] - nums[i - k - 1]
            
            # Use integer division //
            avgs[i] = current_window_sum // window_size
            
        return avgs
