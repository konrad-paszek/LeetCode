from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:x + 1]) for x in range(len(nums))]

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums
