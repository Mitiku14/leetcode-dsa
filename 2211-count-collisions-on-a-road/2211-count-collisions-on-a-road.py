class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for cur in directions:
            if stack and stack[-1] == 'R' and cur == 'L':
                collisions += 2
                stack.pop()    
                cur = 'S'       
            while stack and stack[-1] == 'R' and cur == 'S':
                collisions += 1
                stack.pop()
                
            if stack and stack[-1] == 'S' and cur == 'L':
                collisions += 1
                cur = 'S'
            
            stack.append(cur)
        
        return collisions
