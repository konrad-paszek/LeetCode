class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = "".join([str(digit) for digit in digits])
        res = str(int(res) + 1)
        return [int(i) for i in res]
