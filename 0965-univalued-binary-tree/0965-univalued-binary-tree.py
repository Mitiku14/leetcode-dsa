# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        res = []
        prev = None
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if prev != None and node.val != prev:
                    return False
                prev = node.val
                res.append(node.val)
                

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        
        return all(res[0] == res[i] for i in range(1, len(res)))