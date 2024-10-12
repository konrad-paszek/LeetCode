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