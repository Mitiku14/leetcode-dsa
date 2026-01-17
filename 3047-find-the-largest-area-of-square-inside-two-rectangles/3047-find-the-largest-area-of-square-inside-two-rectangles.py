from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        x1_1, y1_1 = bottomLeft[0]
        x2_1, y2_1 = topRight[0]

        x1_2, y1_2 = bottomLeft[1]
        x2_2, y2_2 = topRight[1]

        left   = max(x1_1, x1_2)
        right  = min(x2_1, x2_2)
        bottom = max(y1_1, y1_2)
        top    = min(y2_1, y2_2)

        width  = right - left
        height = top - bottom
        if width <= 0 or height <= 0:
            return 0 

       
        side = min(width, height)

        return side * side
