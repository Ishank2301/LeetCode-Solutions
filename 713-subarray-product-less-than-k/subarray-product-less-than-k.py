class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k<=1:
            return 0
        left = 0
        product = 1
        count = 0
        for  right in range(n):
            product*=nums[right]
            while product >=k:
                product //=nums[left]
                left+=1
            count+=(right-left+1)
        return count


        """class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0

        prod = 1
        l = 0
        if k <= 1:
            return 0
            
        for r in range(l, len(nums)):
            prod *= nums[r]

            while prod >= k:
                prod //= nums[l]
                l+=1
            
            count += r - l + 1  
        return count"""