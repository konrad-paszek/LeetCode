from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = None
        for index, item in enumerate(nums):
            difference = target - item
            nums[index] = -2
            if difference in nums[index+1:]:
                index_2 = nums.index(difference)
                result = [index, index_2]
        return result


nums = [3,2,3]
target = 6
cl = Solution()
print(cl.twoSum(nums, target))
