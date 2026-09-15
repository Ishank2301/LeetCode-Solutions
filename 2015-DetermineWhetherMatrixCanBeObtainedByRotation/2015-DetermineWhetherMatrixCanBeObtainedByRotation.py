# Last updated: 15/9/2026, 11:34:28 pm
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(matrix):
            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # reverse rows
            for i in range(n):
                matrix[i].reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)

        return False
