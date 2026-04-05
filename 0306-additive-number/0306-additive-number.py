class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(first, second, remaining):
            if not remaining:
                return True
            exp_sum = first + second
            if exp_sum > 0 and remaining[0] == '0':
                return False
            for i in range(1, len(remaining) + 1):
                next_num = int(remaining[:i])
                if next_num == exp_sum:
                    if backtrack(second, exp_sum, remaining[i:]):
                        return True
            return False
        str_len = len(num)
        for first_num_end in range(1, str_len - 1):
            if first_num_end > 1 and num[0] == '0':
                break
            
            for second_num_end in range(first_num_end + 1, str_len):
                if second_num_end - first_num_end > 1 and num[first_num_end] == '0':
                    continue
                
                first_number = int(num[:first_num_end])
                second_number = int(num[first_num_end:second_num_end])
                if backtrack(first_number, second_number, num[second_num_end:]):
                    return True
        return False
                    

            