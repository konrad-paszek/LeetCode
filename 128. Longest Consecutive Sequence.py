from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_result = 0
        nums.sort()
        if len(nums) == 0:
            return 0
        result = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                result += 1
                if result > max_result:
                    max_result = result
            elif nums[i] == nums[i + 1]:
                continue
            else:
                break
        return result

s = Solution()
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
