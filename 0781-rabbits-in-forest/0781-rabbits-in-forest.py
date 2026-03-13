class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        total = 0
        for rabbit, count in cnt.items():

            rabbit_size = rabbit + 1
            groups = math.ceil(count / rabbit_size)
            total += rabbit_size * groups

        return total         