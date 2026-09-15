# Last updated: 15/9/2026, 11:36:26 pm
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # For this kind of questions we need to store the left side product of the element.
        n = len(nums)
        # A result array having 1 elements as the size of array is the same as lenght 0f nums array.
        result = [1]*n
        for i in range(1,n):
            # the result shuld be the element multiplied its next element. 
            # Let's say the righest side element is removed from the list and the result of that is printed
            result[i] = result[i-1] * nums[i-1]
          
        right = 1
        for i in range((n-1), -1, -1):
            result[i] = result[i] * right
            right = nums[i]*right         

        return result

        