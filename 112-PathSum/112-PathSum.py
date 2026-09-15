# Last updated: 15/9/2026, 11:36:57 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

            # check for yhe leaf node:
        if not root.left and not root.right:
            return root.val == targetSum

            # Recursive down the both sides substracting the current value
        remainder  = targetSum - root.val 
        return self.hasPathSum(root.left, remainder) or \
                self.hasPathSum(root.right,remainder)