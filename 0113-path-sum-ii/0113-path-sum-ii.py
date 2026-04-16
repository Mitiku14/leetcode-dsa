# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def dfs(node, cur):
            if not node:
                return 0
            cur.append(node.val)
            temp = cur.copy()
            if not node.left and not node.right:
                if sum(temp) == targetSum:
                    self.res.append(temp)
            left = dfs(node.left, cur)
            right = dfs(node.right, cur)
            cur.pop()
        dfs(root, [])
        return self.res

                