import unittest
from typing import List, Dict, Tuple


# Bruteforce-ish solution : start at the leftmost and rightmost edges,
# check all the potentials solutions with smaller width
# (left more to the right and/or right more to the left)
# skip a 'smaller' solution if height of the new left/right is not higher.
# Could optimize further by determining that it's worth reducing the width by x
# only if the height gain is at least y?
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Contains the biggest possible volume within a left-right range
        # (aka a candidate).
        # could be the volume of a sub-candidate :
        # left and/or right closer to the middle.
        # NOT simply the volume of left-right
        # avoids computing multiple time the same things
        # key : tuple of the left and right index
        # value : biggest possible volume
        seen: Dict[(int, int), int] = dict()

        def compute_volume(left: int, right: int) -> int:
            return min(height[left], height[right]) * (right - left)

        def indexedMaxArea(left: int, right: int) \
                -> Tuple[Tuple[int, int], int]:
            """ Returns the candidate with the biggest volume within left-right.

            :param left: left limit (an index of height)
            :param right: right limit (an index of height)
            :return: best candidate + its volume
            """
            candidate_range = (height[left], height[right])
            if candidate_range in seen:
                # already evaluated this candidate, skip.
                return (candidate_range, seen[candidate_range])
            candidate_volume = compute_volume(left, right)

            # search for next left candidate (if any)
            next_candidate_left = next(
                (candidate_left
                 for candidate_left in range(left + 1, right)
                 if height[candidate_left] > height[left]),
                None)
            if next_candidate_left:
                (best_candidate_left, best_left_volume) = \
                    indexedMaxArea(next_candidate_left, right)
                if best_left_volume > candidate_volume:
                    candidate_range = best_candidate_left
                    candidate_volume = best_left_volume

            # search for next right candidate (if any)
            next_candidate_right = next(
                (candidate_right
                 for candidate_right in range(right - 1, left, -1)
                 if height[candidate_right] > height[right]),
                None)
            if next_candidate_right:
                (best_candidate_right, best_right_volume) = \
                    indexedMaxArea(left, next_candidate_right)
                if best_right_volume > candidate_volume:
                    candidate_range = best_candidate_right
                    candidate_volume = best_right_volume
            seen[left, right] = candidate_volume
            return (candidate_range, candidate_volume)

        return indexedMaxArea(0, len(height) - 1)[1]


# Much simpler solution (looked at the discussion forum)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = -1
        while left < right:
            water = max(water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                # can skip all the solutions left and right-1, right-2, ...
                left += 1
            else:
                right -= 1
        return water

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertMaxArea(self, expected: int, height: List[int]):
        self.assertEqual(expected, self.s.maxArea(height))

    def test_examples(self):
        self.assertMaxArea(49, [1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertMaxArea(1, [1, 1])
        self.assertMaxArea(16, [4, 3, 2, 1, 4])
        self.assertMaxArea(2, [1, 2, 1])

    #@unittest.skip("potential slow execution")
    def test_extremes(self):
        self.assertMaxArea(0, [0, 0])
        self.assertMaxArea(10 ** 4, [10 ** 4, 10 ** 4])
        self.assertMaxArea(10 ** 5 - 1, [1] * 10 ** 5)
