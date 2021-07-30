import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if s.split() else 0

# Other solution without using powerful builtin methods (str.split)
# try to make it faster than the first solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_end = len(s) - 1
        # skip spaces at the end
        while last_word_end >= 0 and s[last_word_end] == ' ':
            last_word_end -= 1

        if last_word_end == -1:
            # empty or only spaces
            return 0

        # search for the start of the last word
        last_word_start = last_word_end - 1
        while last_word_start >= 0 and s[last_word_start] != ' ':
            last_word_start -= 1

        return last_word_end - last_word_start



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertLengthOfLastWord(self,
                               expected: int,
                               s: str) -> None:
        self.assertEqual(expected, self.s.lengthOfLastWord(s))

    def test_examples(self):
        self.assertLengthOfLastWord(5, "Hello World")
        self.assertLengthOfLastWord(0, " ")

    def test_empty(self):
        self.assertLengthOfLastWord(0, "")

    def test_no_space(self):
        self.assertLengthOfLastWord(1, "x")
        self.assertLengthOfLastWord(2, "xx")
        self.assertLengthOfLastWord(3, "xxx")

    def test_multiple_spaces(self):
        self.assertLengthOfLastWord(0, "  ")
        self.assertLengthOfLastWord(0, "   ")
        self.assertLengthOfLastWord(1, "  x")
        self.assertLengthOfLastWord(1, "   x")
        self.assertLengthOfLastWord(2, "  aa  xx")
        self.assertLengthOfLastWord(2, "           xx")

    def test_ends_with_spaces(self):
        self.assertLengthOfLastWord(1, "x ")
        self.assertLengthOfLastWord(1, " x ")
        self.assertLengthOfLastWord(2, "xx ")
        self.assertLengthOfLastWord(2, " xx ")
        self.assertLengthOfLastWord(2, "xx xx ")
        self.assertLengthOfLastWord(2, "xx xx  ")