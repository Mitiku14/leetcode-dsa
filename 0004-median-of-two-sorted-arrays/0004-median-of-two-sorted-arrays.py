class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        return sum(res) / len(res)
        