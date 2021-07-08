# https://leetcode.com/problems/reverse-integer
#Unsupported edge case : number is -2**31 (cause : if negative, flip positive, compute, flip back)
class Solution:
    @staticmethod
    def will_overflow(value, add):
        MAX = 2**31 - 1
        margin = MAX - value
        return add > margin

    @staticmethod
    def can_multiply_by_ten(value):
        MAX_MULTIPLIABLE_BY_TEN = (2**31 - 1) // 10
        return value <= MAX_MULTIPLIABLE_BY_TEN

    def reverse(self, x: int) -> int:
        negative = x<0
        x = abs(x)
        new_x = 0
        while x:
            digit = x % 10
            x = x // 10
            if not self.can_multiply_by_ten(new_x) or self.will_overflow(new_x*10, digit):
                return 0
            new_x = new_x*10 + digit
        new_x= -new_x if negative else new_x
        return new_x

print(Solution().reverse(-123))
