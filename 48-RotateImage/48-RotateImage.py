# Last updated: 15/9/2026, 11:37:33 pm
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1 transpose of the matrix
        """Method of transpose can be switching the columns to row by the specific indexes as we know our matrix is only gonna be a square matrix as in n*n, so we can easily convert or propose a transpose for n*n dimensionality matrix"""

        # we can define it as doing  matrix[r][c] === matrix[c][r] i think this should solve the problem

        # Lets code this
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2 Inverse the columns than it will be rotated
        for i in range(n):
            matrix[i].reverse()
