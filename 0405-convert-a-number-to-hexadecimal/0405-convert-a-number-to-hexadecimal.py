class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        num &= 0xFFFFFFFF
        
        hex_digits = "0123456789abcdef"
        result = []
        
        while num > 0:
            result.append(hex_digits[num % 16])
            num //= 16
        
        return "".join(reversed(result))
