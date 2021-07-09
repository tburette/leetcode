# https://leetcode.com/problems/valid-parentheses/
import unittest


class Solution:
    corresponding_parenthesis = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s: str) -> bool:
        """Determine if the input string has matching brackets ( { [

        :param s: a string consisting of only the characters ()[]{}
        """
        stack = list()
        for c in s:
            if c in Solution.corresponding_parenthesis:
                stack.append(Solution.corresponding_parenthesis[c])
            elif not stack or stack.pop() != c:
                return False
        return not stack


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertIsValid(self, s: str, result: bool):
        self.assertEqual(
            result,
            self.solution.isValid(s))

    def test_examples(self):
        self.assertIsValid("()", True)
        self.assertIsValid("()[]{}", True)
        self.assertIsValid("(]", False)
        self.assertIsValid("([)]", False)
        self.assertIsValid("{[]}", True)

    def test_empty(self):
        self.assertIsValid("", True)

    def test_no_closing(self):
        self.assertIsValid('(', False)
