class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2): # Stop at n-2 because you need 3 numbers
            # 1. Skip duplicate 'i' values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 2. Two-pointer search for the remaining two numbers
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # 3. Move pointers and skip duplicates for j and k
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1 # Sum too small, move left pointer right
                else:
                    k -= 1 # Sum too big, move right pointer left
        return res
