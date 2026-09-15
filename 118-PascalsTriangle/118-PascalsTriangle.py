# Last updated: 15/9/2026, 11:36:52 pm
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # create a row with all 1
            row = [1] * (i + 1)

            #       fill inner elements using DP relation
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle