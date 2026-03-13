class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        count = 0
        while maxDoubles >=1 and target > 1:
            if target % 2 == 0:
                target = target // 2
                count += 1
                maxDoubles -= 1
            else:
                target -= 1
                count += 1


        count += target - 1
        return count