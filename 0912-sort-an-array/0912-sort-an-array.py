class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def merge(left_half, right_half):
            i = 0
            j = 0
            res = []
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    res.append(left_half[i])
                    i += 1
                else:
                    res.append(right_half[j])
                    j += 1
            res.extend(left_half[i:])
            res.extend(right_half[j:])
            return res
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        return mergeSort(0, n -1, nums)
        