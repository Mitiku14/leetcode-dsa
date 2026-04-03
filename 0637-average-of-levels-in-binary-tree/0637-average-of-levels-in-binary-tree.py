# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            total_sum = 0.0
            for _ in range(levelSize):
                curNode = queue.popleft()
                total_sum += curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(total_sum / levelSize)
        return res