class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n-k+1):
            sub = nums[i:i+k]
            cnt = Counter(sub)
            arr = []
            for num, freq in cnt.items():
                arr.append((freq, num))
            
            total = 0
            arr.sort(reverse=True)
            for j in range(min(x, len(arr))):
                freq, num = arr[j]
                total += (freq * num)
            res.append(total)
        
        return res
        
        

            


        
        

            
