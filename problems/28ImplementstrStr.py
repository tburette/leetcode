import unittest


class Solution:
    # Setting ourself an additional constraint :
    # can only access one char at a time through index access.
    # The problem is too easy otherwise.
    # slow, naive algorithm
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j, _ in enumerate(needle):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertStrStr(self, expected: int, haystack: str, needle: str) -> None:
        self.assertEqual(expected, self.s.strStr(haystack, needle))

    def test_examples(self):
        self.assertStrStr(2, "hello", "ll")
        self.assertStrStr(-1, "aaaaa", "bba")
        self.assertStrStr(0, "", "")

    def test_empty_needle(self):
        self.assertStrStr(0, "", "")
        self.assertStrStr(0, "a", "")
        self.assertStrStr(0, "aa", "")

    def test_empty_haystack(self):
        self.assertStrStr(-1, "", "x")
        self.assertStrStr(-1, "", "xx")

    def test_misc(self):
        # extremities
        self.assertStrStr(0, "abc", "a")
        self.assertStrStr(2, "abc", "c")
        # identical
        self.assertStrStr(0, "a", "a")
        self.assertStrStr(0, "abc", "abc")
        # same length no match
        self.assertStrStr(-1, "abc", "abx")
        self.assertStrStr(-1, "abc", "xbc")
        # not found
        self.assertStrStr(-1, "abc", "d")
        # longer
        self.assertStrStr(-1, "abc", "abcd")
        self.assertStrStr(-1, "abc", "dabc")

    def test_big(self):
        self.assertStrStr(-1, "a" * 5000, "a" * 4000 + "x")
