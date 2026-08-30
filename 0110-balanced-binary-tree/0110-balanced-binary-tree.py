# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfsheight(self, root):

        # Empty tree has height 0
        if root is None:
            return 0

        # Find height of left subtree
        leftHeight = self.dfsheight(root.left)

        # If left subtree is unbalanced, return -1
        if leftHeight == -1:
            return -1

        # Find height of right subtree
        rightHeight = self.dfsheight(root.right)

        # If right subtree is unbalanced, return -1
        if rightHeight == -1:
            return -1

        # Current node is unbalanced
        if abs(leftHeight - rightHeight) > 1:
            return -1

        # Return height of current subtree
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Tree is balanced if dfsheight doesn't return -1
        return self.dfsheight(root) != -1