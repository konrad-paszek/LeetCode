from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_to_index:
                return [nums_to_index[target-nums[i]], i]
            nums_to_index[nums[i]] = i
        return []


nums = [3,2,3]
target = 6
cl = Solution()
print(cl.twoSum(nums, target))
