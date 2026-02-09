class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle_num = num // 3
        sum_of_three = (middle_num - 1) + (middle_num) + (middle_num + 1)
        if sum_of_three == num:
            return [middle_num - 1, middle_num, middle_num  + 1]
        return []
