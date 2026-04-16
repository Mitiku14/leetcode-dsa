# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total = -inf
        def dfs(node):
            if not node:
                return -inf
            left = dfs(node.left)
            right = dfs(node.right)
            v = node.val
            self.total = max(self.total, v, v + left, v + right, v + left + right)
            return max(v , v + left, v + right)
        dfs(root)
        return self.total
