class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for n in range(len(nums) + 1)]
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for c, v in count.items():
            freq[v].append(c)
        for item in freq[::-1]:
            for i in item:
                res.append(i)
                if len(res) == k:
                    return res

