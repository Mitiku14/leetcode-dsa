from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        q = deque([root])
        while q:
            size = len(q)
            found_x = False
            found_y = False

            for _ in range(size):
                node = q.popleft()
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False
                if node.left:
                    q.append(node.left)
                    if node.left.val == x:
                        found_x = True
                    if node.left.val == y:
                        found_y = True

                if node.right:
                    q.append(node.right)
                    if node.right.val == x:
                        found_x = True
                    if node.right.val == y:
                        found_y = True
            if found_x and found_y:
                return True
            if found_x or found_y:
                return False

        return False