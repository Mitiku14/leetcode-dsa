# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, par, gpar):
            nonlocal ans
            if not node:
                return 
            if gpar % 2 == 0 and gpar != -1:
                ans += node.val
            
            dfs(node.left, node.val, par)
            dfs(node.right, node.val, par)
        dfs(root, -1, -1)

        return ans
        