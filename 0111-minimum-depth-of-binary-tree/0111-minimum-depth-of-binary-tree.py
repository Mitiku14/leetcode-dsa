# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_dep = 0
        queue = deque()
        queue.append(root)
        while queue:
            min_dep += 1
            level_size = len(queue)
            for _ in range(level_size):
                curNode = queue.popleft()
                if not curNode.left and not curNode.right:
                    return min_dep
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            