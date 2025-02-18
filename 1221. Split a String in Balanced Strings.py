class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        res = 0
        for letter in s:
            if letter == "R":
                r += 1
            elif letter == "L":
                l += 1
            if r != 0 and r == l:
                res += 1
                r = 0
                l = 0
        return res
