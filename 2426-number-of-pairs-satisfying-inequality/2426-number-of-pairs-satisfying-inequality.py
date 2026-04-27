from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        n = len(nums1)
        sl = SortedList()
        for i in range(n):
            temp = sl.bisect_right(nums1[i] - nums2[i] + diff)
            count += temp
            sl.add(nums1[i] - nums2[i])
        return count

                