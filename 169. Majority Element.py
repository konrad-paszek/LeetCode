class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if  i == res:
                count += 1
            else:
                if count == 0:
                    res = i
                    count += 1
                else:
                    count -= 1
        return res
