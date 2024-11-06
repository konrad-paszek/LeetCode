class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i, item in enumerate(s):
            index = t.index(item)
            result += abs(i - index)
        return result