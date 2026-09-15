# Last updated: 15/9/2026, 11:36:41 pm
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        i, j = 0, n - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]
            
            elif current_sum < target:
                i += 1
                
            else:
                j -= 1
        
        return []
