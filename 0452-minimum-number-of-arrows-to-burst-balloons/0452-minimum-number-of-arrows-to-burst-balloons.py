class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)
        min_num_arrow = 1
        shoted_arrow = points[0][1]

        for i in range(1, len(points)):
            print(points[i][0], shoted_arrow)
            if points[i][0] > shoted_arrow:
                min_num_arrow += 1
                shoted_arrow = points[i][1]
        return min_num_arrow
            

