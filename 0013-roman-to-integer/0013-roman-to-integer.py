class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            'I': 1, 'V' : 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000
        }
        Sum = 0
        i = 0 
        n = len(s)
        while i < n:
            if i < n-1 and roman_numbers[s[i]] < roman_numbers[s[i +1]]:
                Sum += roman_numbers[s[i+1]] - roman_numbers[s[i]]
                i +=2
            else:
                Sum += roman_numbers[s[i]]
                i += 1
        return Sum
            
            