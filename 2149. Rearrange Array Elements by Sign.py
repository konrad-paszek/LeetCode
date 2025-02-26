from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        minus = [x for x in nums if x < 0]
        plus = [x for x in nums if x > 0]
        for i in range(len(nums)):
            if i & 1:
                res.append(minus.pop(0))
            else:
                res.append(plus.pop(0))

        return res

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        return ans



s = Solution()

print(s.rearrangeArray([28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]))