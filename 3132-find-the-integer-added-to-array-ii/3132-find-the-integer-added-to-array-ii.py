class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        nums1.remove(nums1[0])
        nums1.remove(nums1[0])
        # print(nums1)
        return nums2[0] - nums1[0]


        
        




        