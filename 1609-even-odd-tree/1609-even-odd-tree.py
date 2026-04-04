class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        queue = deque([root])
        level_ind = 0
        
        while queue:
            level_size = len(queue)
            prev = None
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Even level
                if level_ind % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev is not None and node.val <= prev:
                        return False
                # Odd level
                else:
                    if node.val % 2 == 1:
                        return False
                    if prev is not None and node.val >= prev:
                        return False
                
                prev = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_ind += 1
        
        return True