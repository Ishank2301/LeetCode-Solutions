# Last updated: 15/9/2026, 11:37:23 pm
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        col_start, col_end = 0, m - 1
        row_start, row_end = 0, n - 1
        ans = []
        
        # Continue until we have visited all elements
        while len(ans) < n * m:
            # 1. Traverse Right: Row_start (fixed), Column_start -> Column_end
            for i in range(col_start, col_end + 1):
                ans.append(matrix[row_start][i])
            row_start += 1
            if len(ans) == n * m: break
            
            # 2. Traverse Down: Column_end (fixed), Row_start -> Row_end
            for i in range(row_start, row_end + 1):
                ans.append(matrix[i][col_end])
            col_end -= 1
            if len(ans) == n * m: break
            
            # 3. Traverse Left: Row_end (fixed), Col_end -> Col_start (reverse)
            for i in range(col_end, col_start - 1, -1):
                ans.append(matrix[row_end][i])
            row_end -= 1
            if len(ans) == n * m: break
            
            # 4. Traverse Up: Col_start (fixed), Row_end -> Row_start (reverse)
            for i in range(row_end, row_start - 1, -1):
                ans.append(matrix[i][col_start])
            col_start += 1
            
        return ans
