class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        piv = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
                
            elif num == pivot:
                piv.append(num)
                
            else:
                greater.append(num)
                
        less.extend(piv)
        less.extend(greater)
        return less
        
            