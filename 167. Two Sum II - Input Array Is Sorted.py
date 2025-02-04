from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = 1
        while L < R:
            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1]
            else:
                if R == len(numbers) - 1:
                    L += 1
                    R = L + 1
                else:
                    R += 1

s = Solution()
s.twoSum([5,25,75], 100)