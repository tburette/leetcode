import unittest
from typing import List


# Solution comes from TDD :
# algorithm altered progressively to take into account new cases
# The result is too complex/ugly because new cases only added code and
# never removed any
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0  # left index
        j = len(nums) - 1  # right index
        if i == j:
            # only one element, will never enter the loop
            middle = i
        while i != j:
            middle = i + (j - i) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                if j == middle:
                    break
                j = middle
            else:
                if i == middle:
                    i += 1
                    middle += 1
                i = middle

        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return middle
        else:
            return middle

# cleaner solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = low + (high-low)//2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle
            else:
                low = middle + 1

        if nums[low] < target:
            return low + 1
        return low

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertSearchInsert(self,
                           expected: int,
                           nums: List[int],
                           target: int) -> None:
        self.assertEqual(expected, self.s.searchInsert(nums, target))

    def test_examples(self):
        self.assertSearchInsert(2, [1, 3, 5, 6], 5)
        self.assertSearchInsert(1, [1, 3, 5, 6], 2)
        self.assertSearchInsert(4, [1, 3, 5, 6], 7)
        self.assertSearchInsert(0, [1, 3, 5, 6], 0)
        self.assertSearchInsert(0, [1], 0)

    def test_size_one(self):
        self.assertSearchInsert(0, [1], 0)
        self.assertSearchInsert(1, [1], 2)

    def test_size_two(self):
        self.assertSearchInsert(0, [1, 3], 0)
        self.assertSearchInsert(0, [1, 3], 1)
        self.assertSearchInsert(1, [1, 3], 2)
        self.assertSearchInsert(1, [1, 3], 3)
        self.assertSearchInsert(2, [1, 3], 4)

    def test_size_three(self):
        self.assertSearchInsert(0, [1, 3, 5], 1)
        self.assertSearchInsert(1, [1, 3, 5], 2)
        self.assertSearchInsert(1, [1, 3, 5], 3)
        self.assertSearchInsert(2, [1, 3, 5], 4)
