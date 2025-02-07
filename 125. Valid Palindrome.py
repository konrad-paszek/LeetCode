class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L = 0
        R = len(s) - 1
        while L < R:
            if not s[L].isalpha():
                L += 1
                continue
            if not s[R].isalpha():
                R -= 1
                continue
            if s[L] != s[R]:
                return False
            L, R = L + 1, R - 1

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L = 0
        R = len(s) - 1
        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if s[L] != s[R]:
                return False
            L, R = L + 1, R - 1

        return True

s = Solution()
s.isPalindrome("0P")