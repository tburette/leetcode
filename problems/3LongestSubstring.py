# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def max_non_repeating_prefix_len(substring: str):
            seen_chars = set()
            for c in substring:
                if c in seen_chars:
                    break
                seen_chars.add(c)
            return len(seen_chars)
        # all substrings where only the beginning moves (substring end == s end)
        substrings_left = [s[i:] for i in range(len(s))]
        return max(max_non_repeating_prefix_len(substring_left) for substring_left in substrings_left)


print(Solution().lengthOfLongestSubstring("xabcdaa"))
