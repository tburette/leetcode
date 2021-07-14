import unittest
from collections import Counter
from typing import List


class Solution:
    # the example 1 of the problem statement seems to hint at an algorithm
    # that scans left to right for for element to remove
    # AND scans right to left for values to keep
    # putting a value to keep (from the right)
    # in an element to remove (on the left).
    # That algorithm would run until both scan (l-to-r and r-to-l) meet.
    # This algorithm does NOT do that. It simply goes left to right
    # and put in the next available index (filered_index+1) any value to keep
    # (the value is different from the arg val).
    # The hinted algorithm results in fewer writes.
    # My algorithm _might_ have better cache efficiency :
    #   strictly left-to-right progress (for reading and writing)
    #   vs left-to-right and right-to-left pattern for the hinted algorithm
    def removeElement(self, nums: List[int], val: int) -> int:
        # invariant : elements [0:filtered_index] are elements from which
        # val has been filtered-out
        filtered_index = 0
        for value in nums:
            if value != val:
                nums[filtered_index] = value
                filtered_index += 1
        # +1 because must return the count not the last index,2
        return filtered_index


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertRemoveElement(
            self,
            expected_nums: List[int],
            nums: List[int],
            val: int):
        k = self.s.removeElement(nums, val)
        self.assertEqual(len(expected_nums), k)
        self.assertGreaterEqual(
            len(nums),
            len(expected_nums),
            "nums is too small")
        self.assertEqual(
            Counter(expected_nums),
            Counter(nums[:k]),
            "nums[:k] does not contain the expected value (in any order)")

    def test_examples(self):
        self.assertRemoveElement([2, 2], [3, 2, 2, 3], 3)
        self.assertRemoveElement([0, 1, 4, 0, 3], [0, 1, 2, 2, 3, 0, 4, 2], 2)

    def test_empty(self):
        self.assertRemoveElement([], [], 0)

    def test_remove_all(self):
        self.assertRemoveElement([], [2], 2)
        self.assertRemoveElement([], [2, 2], 2)
        self.assertRemoveElement([], [2, 2, 2], 2)

    def test_remove_none(self):
        self.assertRemoveElement([1], [1], 2)
        self.assertRemoveElement([1, 2, 3], [1, 2, 3], 0)

    def test_remove_extremities(self):
        self.assertRemoveElement([2, 3], [1, 2, 3], 1)
        self.assertRemoveElement([1, 2], [1, 2, 3], 3)

    def test_remove_internal(self):
        self.assertRemoveElement([1, 2, 3], [1, 0, 2, 0, 3], 0)
        self.assertRemoveElement([1, 3], [1, 0, 0, 0, 3], 0)
