class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        res2 = []
        for num in arr2:
            if num in arr2 and num in freq:
                res.extend([num] * freq[num])
        for num in arr1:
            if num not in arr2:
                res2.append(num)
        res2.sort()
        return res + res2
        
        

