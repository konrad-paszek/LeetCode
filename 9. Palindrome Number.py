class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            palindrome = int(str(x)[::-1])
            return x == palindrome
        return False