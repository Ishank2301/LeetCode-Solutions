# Last updated: 15/9/2026, 11:37:19 pm
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix and boundaries
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        
        # Fill matrix in spiral order until num exceeds n^2
        while num <= n * n:
            # Right, Down, Left, Up, updating boundaries after each side
            for i in range(left, right + 1):
                matrix[top][i] = num; num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num; num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num; num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num; num += 1
            left += 1
            
        return matrix
