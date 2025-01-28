from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        sufix = [1] * (n - 1) + [nums[-1]]
        res = []
        for i in range(1, n):
            prefix.append(nums[i] * prefix[i - 1])
        for i in range(n - 2, 0, -1):
            sufix[i] = sufix[i + 1] * nums[i]
        res.append(sufix[1])
        for i in range(1, n - 1):
            res.append(prefix[i - 1] * sufix[i + 1])
        res.append(prefix[-1])
        return res


s = Solution()
s.productExceptSelf([1,2,3,4])