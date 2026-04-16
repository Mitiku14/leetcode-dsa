# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        def dfs(node, cur):
            if not node:
                return 
            cur.append(str(node.val))
            # print(cur)
            if not node.left and not node.right:
                temp = '->'.join(cur)
                self.res.append(temp)
            else:
                left = dfs(node.left, cur)
                right = dfs(node.right, cur)
            cur.pop()
        
        dfs(root, [])
        return self.res