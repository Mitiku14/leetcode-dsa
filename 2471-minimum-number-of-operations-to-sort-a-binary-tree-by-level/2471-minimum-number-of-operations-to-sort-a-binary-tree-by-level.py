# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(arr):
            n = len(arr)
            temp = [(val, ind) for ind, val in enumerate(arr)]
            temp.sort()
            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or temp[i][1] == i:
                    continue
                
                cy_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = temp[j][1]
                    cy_size += 1
                
                if cy_size > 1:
                    swaps += cy_size - 1
            return swaps


        q = deque([root])
        min_op = 0
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            min_op += min_swaps(level)
        return min_op