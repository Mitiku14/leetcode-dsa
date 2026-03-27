# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if not node:
                return 
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            l = dfs(node.left)
            if l:
                return True
            
            r = dfs(node.right)
            if r:
                return True
            
            return False
        return dfs(root)


        