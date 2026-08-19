class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0
        
        while i < n or j < n:
            # 1. Advance pointer 'i' to the next real letter in start
            while i < n and start[i] == '_':
                i += 1
                
            # 2. Advance pointer 'j' to the next real letter in target
            while j < n and target[j] == '_':
                j += 1
            
            # If one string ends but the other still has letters left
            if (i == n) != (j == n):
                return False
                
            # If both reached the end successfully, we are done
            if i == n and j == n:
                return True
            
            # Rule 1: The letters must match in order
            if start[i] != target[j]:
                return False
                
            # Rule 2: 'L' cannot move right (start index must be >= target index)
            if start[i] == 'L' and i < j:
                return False
                
            # Rule 3: 'R' cannot move left (start index must be <= target index)
            if start[i] == 'R' and i > j:
                return False
            
            # Move to the next characters
            i += 1
            j += 1
            
        return True

