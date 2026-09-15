# Last updated: 15/9/2026, 11:35:28 pm
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]
