# https://leetcode.com/problems/roman-to-integer
import unittest
import itertools

class Solution:
    value_of_numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # combinations where the first numeral indicates
    # a subtraction from the second numeral
    subtractions = {
        ('I', 'V'),
        ('I', 'X'),
        ('X', 'L'),
        ('X', 'C'),
        ('C', 'D'),
        ('C', 'M')
    }

    def romanToInt(self, s: str) -> int:
        def value(numeral, next_numeral):
            # could check if the value of numeral is smaller than next_numeral
            # instead of using subtractions
            if (numeral, next_numeral) in Solution.subtractions:
                # numeral is a subtraction from next_numeral
                # eg. IV :
                #   numeral = I, next_numeral = V
                #   if subtract 1 instead of adding (and later add 5) we'll get
                #   the correct value
                return -Solution.value_of_numeral[numeral]
            else:
                return Solution.value_of_numeral[numeral]
        # for the last char: n = last_char, n2 = None (cf zip_longest)
        return sum([value(n, n2) for n, n2 in itertools.zip_longest(s, s[1:])])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.romanToInt("III"), 3)

    def test_example_2(self):
        self.assertEqual(self.s.romanToInt("IV"), 4)

    def test_example_3(self):
        self.assertEqual(self.s.romanToInt("IX"), 9)

    def test_example_4(self):
        self.assertEqual(self.s.romanToInt("LVIII"), 58)

    def test_example_5(self):
        self.assertEqual(self.s.romanToInt("MCMXCIV"), 1994)
