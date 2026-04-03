"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        max_dep = 0
        temp = 0
        while queue:
            level_size = len(queue)
            temp += 1
            for _ in range(level_size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            max_dep = max(max_dep, temp)
        return max_dep
        
        