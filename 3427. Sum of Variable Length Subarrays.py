from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
        return sum(prefix_sum)


s = Solution()
s.subarraySum([2,3,1])