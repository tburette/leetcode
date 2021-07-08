# https://leetcode.com/problems/longest-common-prefix
import unittest
from itertools import takewhile
from typing import List


# v1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def all_identicals(iter):
            return len(set(iter)) == 1

        def take_first(iter):
            return [elem[0] for elem in iter]

        return ''.join(take_first(takewhile(all_identicals, zip(*strs))))


# v2 same as v1 but more readable
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def all_identicals(iter):
            return len(set(iter)) == 1

        def take_first(iter):
            return [elem[0] for elem in iter]

        # if strs = ["ab", "xyz"] then:
        #   letter_by_letter = [("a", "x"), ("b", "y")]
        letter_by_letter = zip(*strs)
        letter_by_letter_common_prefix = takewhile(
            all_identicals,
            letter_by_letter)
        return ''.join(take_first(letter_by_letter_common_prefix))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertLongestCommonPrefix(self, strs: List[str], result: str):
        self.assertEqual(
            self.solution.longestCommonPrefix(strs), result)

    def test_examples(self):
        self.assertLongestCommonPrefix(["flower", "flow", "flight"], "fl")
        self.assertLongestCommonPrefix(["dog", "racecar", "car"], "")

    def test_one_string(self):
        self.assertLongestCommonPrefix(["string"], "string")

    def test_empty_string(self):
        self.assertLongestCommonPrefix([""], "")
        self.assertLongestCommonPrefix(["", ""], "")

    def test_all_identical(self):
        self.assertLongestCommonPrefix(["hello", "hello"], "hello")
