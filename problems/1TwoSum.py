# https://leetcode.com/problems/two-sum/
from typing import List
import itertools


# Basic version, try all possible combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (i, j) in itertools.combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of_val = {v: i for (i, v) in enumerate(nums)}
        for (i, v) in enumerate(nums):
            complement_value = target - v
            if complement_value in index_of_val and index_of_val[complement_value] != i:
                return [i, index_of_val[complement_value]]
