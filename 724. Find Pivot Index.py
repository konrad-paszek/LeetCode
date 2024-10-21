from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_presums = nums[:]
        right_presums = nums[:]
        for i in range(len(nums) - 1):
            left_presums[i + 1] += left_presums[i]
        for i in range(len(nums) - 1, 0, -1):
            right_presums[i - 1] += right_presums[i]
        for i in range(len(nums)):
            if left_presums[i] == right_presums[i]:
                return i - 1
        return - 1

obj = Solution()
nums = [1,7,3,6,5,6]
print(obj.pivotIndex(nums))