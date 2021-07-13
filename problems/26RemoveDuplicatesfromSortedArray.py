import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_value = -101  # outside the range of admitted values
        k = -1  # k is the index of the last non-duplicated value in nums
        for value in nums:
            if value != current_value:
                k += 1
                current_value = value
                nums[k] = current_value
            # if value == current_value:
            #   Nothing to do (except incrementing the index)
        return k + 1  # +1 because we want the count no the last index


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertRemoveDuplicates(self, expected_nums, nums):
        k = self.s.removeDuplicates(nums)
        self.assertEqual(len(expected_nums), k)
        for i, value in enumerate(expected_nums):
            self.assertEqual(value, nums[i])

    def test_examples(self):
        self.assertRemoveDuplicates([1, 2], [1, 1, 2])
        self.assertRemoveDuplicates([0, 1, 2, 3, 4],
                                    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

    def test_empty(self):
        self.assertRemoveDuplicates([], [])

    def test_one_value(self):
        self.assertRemoveDuplicates([1], [1])

    def test_only_duplicates(self):
        self.assertRemoveDuplicates([1], [1, 1, 1])
        self.assertRemoveDuplicates([1], [1, 1])
        self.assertRemoveDuplicates([0], [0, 0])

    def test_no_duplicates(self):
        self.assertRemoveDuplicates([1, 2], [1, 2])
        self.assertRemoveDuplicates([1, 2, 3], [1, 2, 3])
        self.assertRemoveDuplicates([-1, 0, 3, 4], [-1, 0, 3, 4])

    def test_negatives(self):
        self.assertRemoveDuplicates([-5, -3, -1], [-5, -5, -3, -1, -1])
