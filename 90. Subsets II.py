class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        result = []
        for num in nums:
            res += [ x + [num] for x in res]
        for item in res:
            item.sort()
        for item in res:
            if item not in result:
                result.append(item)
        return result