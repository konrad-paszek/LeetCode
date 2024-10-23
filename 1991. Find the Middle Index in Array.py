from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
            return - 1



obj = Solution()
print(obj.findMiddleIndex([2,3,-1,8,4]))