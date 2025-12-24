class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApple = sum(apple)
        total = 0
        capacity.sort(reverse=True) 
        count = 0
        for r in capacity:
            total += r
            count += 1
            if total >= totalApple:
                return count
            
        
        