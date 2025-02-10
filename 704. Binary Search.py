from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)
        while L != R:
            middle = L + ((R - L) // 2)
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                L = middle + 1
            else:
                R = middle
        return -1

s = Solution()
s.search([-1,0,3,5,9,12], 9)