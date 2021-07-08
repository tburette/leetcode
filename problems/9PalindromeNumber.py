# https://leetcode.com/problems/palindrome-number
import math
import unittest


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         return s == ''.join(reversed(s))

# class Solution:
#     @staticmethod
#     def remove_first_digit(x: int) -> int:
#         if x < 0:
#             raise ValueError(f'Number must be a positive int. {x} given')
#         digits_to_remove = math.floor(math.log10(x))
#         return x // 10**digits_to_remove
#
#     @staticmethod
#     def remove_first_and_last_digit(x: int) -> int:
#         """Extract first and last digit of x.
#
#         Does nothing if x has less than two digits
#         1 -> 1
#         12 -> 0
#         123 -> 2
#         1234 -> 23
#         ..."""
#         x = Solution.remove_first_digit(x)
#         if x >= 10:
#             x = x%10
#         return x
#
#     # can fail if there are zeros: 1021 -> 2 -> True :(. Use index system instead
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         while abs(x) >= 10:
#             last_digit = x%10
#             first_digit = Solution.remove_first_digit(x)
#             if last_digit != first_digit:
#                 return False
#             x = Solution.remove_first_and_last_digit(x)
#         return True

class Solution:
    def nth_digit(self, x: int, digit) -> int:
        """returns the nth digit of an int.

        digit=0 : return the rightmost digit
        digit=1 : return the second from the right digit
        ..."""
        shifted_right_x = x // 10 ** digit
        return shifted_right_x % 10

    def isPalindrome(self, x: int) -> bool:
        """is x a palindrome.

        Uses an index system to access the digits : 0 is the right most digit,
        1 is the tens place, 2 is the hundreds place,..."""
        if x < 0:
            return False
        if x == 0:
            return True # special case because can't do log(0)
        left_index = math.floor(math.log10(x))
        right_index = 0
        while left_index > right_index:
            if self.nth_digit(x, left_index) != self.nth_digit(x, right_index):
                return False
            left_index -= 1
            right_index += 1

        return True


print(Solution().isPalindrome(11))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_zero(self):
        self.assertTrue(self.s.isPalindrome(0))

    def test_single_digit(self):
        for i in range(1, 10):
            self.assertTrue(self.s.isPalindrome(i))

    def test_negative(self):
       self.assertFalse(self.s.isPalindrome(-1))
       self.assertFalse(self.s.isPalindrome(-9))
       self.assertFalse(self.s.isPalindrome(-10))
       self.assertFalse(self.s.isPalindrome(-11))

    def test_contains_zero(self):
        """zero inside"""
        self.assertTrue(self.s.isPalindrome(101))
        self.assertFalse(self.s.isPalindrome(1021))
