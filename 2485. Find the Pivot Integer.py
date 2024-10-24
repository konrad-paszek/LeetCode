class Solution:
    def pivotInteger(self, n: int) -> int:
        nums_list = list(range(1, n + 1))
        for index, item in enumerate(nums_list):
            if sum(nums_list[:index]) == sum(nums_list[:index:-1]):
                return nums_list[index]
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1, n + 1))
        left_presums = nums[:]
        right_presums = nums[:]
        for i in range(len(nums) - 1):
            left_presums[i+1] += left_presums[i]
        for i in range(len(nums) - 1, 0, -1):
            right_presums[i - 1] += right_presums[i]
        for i in range(len(nums)):
            if right_presums[i] == left_presums[i]:
                return nums[i]
        return -1





n = 8
obj = Solution()
print(obj.pivotInteger(n))


