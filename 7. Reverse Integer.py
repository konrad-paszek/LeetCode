import math


class Solution:
    def reverse(self, x: int) -> int:
        reversed_string = str(x)[::-1]
        if x < 0:
            result = "-" + reversed_string[:-1]
        else:
            result = reversed_string
        if -2**31 > int(result) or int(result) > 2**31:
            return 0
        return int(result)


class Solution:
    def reverse(self, x: int):
        res = 0
        while x:
            digit = int(math.fmod(x ,10))
            x = int(x / 10)
            res = (res * 10) + digit
            if res >= 2 ** 31 or res <= -2**31:
                return 0
        return res

y = Solution()

print(y.reverse(123))