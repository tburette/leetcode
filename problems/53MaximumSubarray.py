import unittest
from typing import List

# WRONG. Doesn't work with negative values in some negative scenarios
# [10, -1, -10,  1, 2, 3] would exclude 10 because discarding 10 - 1 - 10 sounds
# like an improvement (0 if discard -11 if not)
class Solution:
    # gist of the solution:
    #   move left-to-right to search the start
    #   do the same right-to-left
    # The result we are looking for is a subarray, we search for the left index
    # and the right index of that subarray.
    # To find the left index of the max subarray we start with the left of the
    # entire array as the candidate left index of the subarray.
    # Then we move to the right looking for a left index that would result
    # in a better subarray than the current candidate.
    # To determine if an index is an improvement we track the sum of the values
    # between the existing best candidate and the current index
    # (the sum of the value we would exclude if we were to use the index) :
    # if the sum is negative it means it's worth it to exclude the value before
    # the current index from the result => we have found a better candidate.
    # We go through this search until we reached the end of the array.
    # The same process is then repeated with the right index.
    # at the end return the sum of the subarray

    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0

        # my approach doesn't work when the numbers are all non-positive :(
        max_element = max(nums)
        if max_element <= 0:
            return max_element

        # candidate for left of solution, index included in the solution
        candidate_left = 0
        # candidate for right of solution, index excluded from the solution
        candidate_right = len(nums)

        # look for the best candidate_left

        # i : index potentially better than the current candidate_left.
        i = candidate_left + 1
        # keep a sum of the values between candidate_left and
        # before the current index(i).
        # If it ever becomes negative it means it's better to not use
        # the values between candidate_left and the left of i :
        # i becomes the new candidate
        improvement = 0

        while i < candidate_right:
            improvement += nums[i-1]
            # changing the candidate or not if the improvement is zero won't
            # affect the return value (the sum) but it affects the size of
            # the subarray : move forward if 0 to have a smaller subarray
            # (faster for the final sum).
            if improvement <= 0:
                candidate_left = i
                improvement = 0
            i += 1

        # look for the best candidate_right
        i = candidate_right - 1
        improvement = 0
        while i > candidate_left:
            improvement += nums[i]
            if improvement <= 0:
                candidate_right = i
                improvement = 0
            i -= 1

        return sum(nums[candidate_left:candidate_right])


# brute-force
# test all possible subarrays
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0
        best_max = float('-inf')  # best so far
        for from_ in range(0, len(nums)):  # from included
            max_current_from = 0  # best seen so far for current from_
            for to in range(from_+1, len(nums)+1):  # to excluded
                # instead of doing a sum(nums[from, to]) :
                # the best possible subarray for [from, to) is either
                # the new (last) element (as if throwing away previous start)
                # or
                # the previous best + this one (as if keep previous start)
                max_current_from = max(nums[to-1], max_current_from + nums[to-1])
                if max_current_from > best_max:
                    best_max = max_current_from
        return best_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0
        best_max_so_far = float('-inf')
        max_sum_ending_with_x = 0
        for x in nums:
            # the max subarray ending with the current x is either
            # -only x
            # -the best subarray ending at the x of theprevious iteration + x
            max_sum_ending_with_x = max(x, max_sum_ending_with_x + x)
            best_max_so_far = max(best_max_so_far, max_sum_ending_with_x)
        return best_max_so_far


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertMaxSubArray(self,
                          expected: int,
                          nums: List[int]) -> None:
        self.assertEqual(expected, self.s.maxSubArray(nums))

    def test_examples(self):
        self.assertMaxSubArray(6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertMaxSubArray(1, [1])
        self.assertMaxSubArray(23, [5, 4, -1, 7, 8])

    def test_negative(self):
        self.assertMaxSubArray(-1, [-1, -2, -3])
        self.assertMaxSubArray(-1, [-2, -1, -3])
        self.assertMaxSubArray(-1, [-3, -2, -1])

    def test_take_all_in_solution(self):
        self.assertMaxSubArray(3, [1, 2])
        self.assertMaxSubArray(6, [1, 2, 3])
        self.assertMaxSubArray(2, [1, 0, 0, 0, 1])

    def test_increasing_or_decreasing(self):
        self.assertMaxSubArray(15, [1, 2, 3, 4, 5])
        self.assertMaxSubArray(15, [-1, 0, 1, 2, 3, 4, 5])
        self.assertMaxSubArray(15, [5, 4, 3, 2, 1])
        self.assertMaxSubArray(15, [5, 4, 3, 2, 1, 0, -1])

    def test_increasing_then_decreasing(self):
        self.assertMaxSubArray(9, [1, 2, 3, 2, 1])
        self.assertMaxSubArray(8, [1, 2, 3, 2])
        self.assertMaxSubArray(4, [0, 1, 2, 1, 0])
        self.assertMaxSubArray(4, [-1, 0, 1, 2, 1, 0, -1])

    def test_decreasing_then_increasing(self):
        self.assertMaxSubArray(11, [3, 2, 1, 2, 3])
        self.assertMaxSubArray(6, [2, 1, 0, 1, 2])
        self.assertMaxSubArray(1, [1, 0, -1, 0, 1])
        self.assertMaxSubArray(4, [3, 1, 0, -1, 0, 1])
        self.assertMaxSubArray(4, [1, 0, -1, 0, 1, 3])

    def test_min_max_items_value(self):
        min_value = -10 ** 5
        max_value = 10 ** 5
        self.assertMaxSubArray(min_value, [min_value])
        self.assertMaxSubArray(max_value, [max_value])
        self.assertMaxSubArray(min_value, [min_value] * 2)
        self.assertMaxSubArray(max_value * 2, [max_value] * 2)
        self.assertMaxSubArray(max_value, [min_value, max_value])

    # @unittest.skip("slow test")
    def test_max_size(self):
        self.assertMaxSubArray(0, [0] * (3 * 10 ** 4))

    def test_must_not_always_skip_negative(self):
        # correct to exclude -1
        self.assertMaxSubArray(0, [-1, -2, -3, 0, -4, -5])
        # error to exclude -1
        self.assertMaxSubArray(-1, [-1, -2, -3, -4, -5])
        # correct to exclude -5
        self.assertMaxSubArray(-1, [-5, -4, -3, -2, -1])

        # must not exclude a negative value if there only are
        # lower values after?

        # error to exclude 10 (and before)
        self.assertMaxSubArray(10, [10, -1, -10,  1, 2, 3])

        # must not exclude a set of values if the value after are
        # lower than the sum of values before (improvement)
        # reformulated :
        # there must be a value higher or equal to improvement

        # look on both left and right for each iteration?
        # move the one that gives the greater benefit?
        self.assertMaxSubArray(4, [-10, 0, 1, 2, 1, 0, -1])
