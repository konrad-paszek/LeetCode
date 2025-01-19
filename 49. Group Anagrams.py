from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]


s = Solution()
print(s.groupAnagrams(strs))