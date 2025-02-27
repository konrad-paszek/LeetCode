from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        i = 0
        j = 1
        k = 2
        while i <= len(nums) - 3:
            if k == len(nums):
                j += 1
                k = j + 1
            if j == len(nums) - 1:
                i += 1
                j = i + 1
                if j != len(nums) - 1:
                    k = j + 1
                else:
                    break
            if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                result += 1
            k += 1
        return result


s = Solution()

print(s.arithmeticTriplets([0, 1, 2], 1))