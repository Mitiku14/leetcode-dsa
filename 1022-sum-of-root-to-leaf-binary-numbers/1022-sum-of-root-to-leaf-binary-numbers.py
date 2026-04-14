# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def dfs(node, path):
            nonlocal res
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right:
                temp = ''.join(map(str, path))
                ans = int(temp, 2)
                res += ans
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return res

