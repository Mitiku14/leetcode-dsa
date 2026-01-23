class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            low = x - d
            high = x + d
            left, right = 0, len(arr2) - 1
            found = False
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] < low:
                    left = mid + 1
                elif arr2[mid] > high:
                    right = mid - 1
                else:
                    found = True
                    break
            if not found:
                count += 1
        return count
