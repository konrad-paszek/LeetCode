class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return sum(range(n)) - sum(nums)