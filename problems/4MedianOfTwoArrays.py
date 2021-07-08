# https://leetcode.com/problems/median-of-two-sorted-arrays
from typing import List


class Solution:
    # NOT O(log (m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) == 0:
            return 0 # unspecified
        if not (len(nums) / 2).is_integer():
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))