from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1

        return nums[:L]



s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))