from typing import List


# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def sumRange(self, left: int, right: int) -> int:
#         subarray = 0
#         for i in range(left, right+1):
#             subarray += self.nums[i]
#         return subarray



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.presums = nums
        for i in range(len(nums) - 1):
            self.presums[i+1] += self.presums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presums[right]
        return self.presums[right] - self.presums[left-1]


# Your NumArray object will be instantiated and called as such:
nums = [1, 7, 3, 5, 2, 1]
obj = NumArray(nums)
param_1 = obj.sumRange(1,2)
print(param_1)