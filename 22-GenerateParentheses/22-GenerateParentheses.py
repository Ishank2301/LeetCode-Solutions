# Last updated: 15/9/2026, 11:38:13 pm
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
	    def dfs(left, right, s):
		    if len(s) == n * 2:
			    res.append(s)
			    return 

		    if left < n:
			    dfs(left + 1, right, s + '(')

		    if right < left:
			    dfs(left, right + 1, s + ')')

	    res = []
	    dfs(0, 0, '')
	    return res