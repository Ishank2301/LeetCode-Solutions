# Last updated: 15/9/2026, 11:35:51 pm
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # average =  nums[0]+_______+nums[k]/k
        # avg = sum()/k
        # Computible_avg = (avg*k-nums[last_start] + nums[new_end])/k
        curr_sum = 0
        n = len(nums)
        for i in range(k):
            curr_sum += nums[i] 
            ans = curr_sum/k

        for  i in range(k,n):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            ans = max(ans,curr_sum/k)
        return ans