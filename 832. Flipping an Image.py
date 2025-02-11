from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for j in range(len(i)):
                i[j] ^= 1
        return image

image = [[1,1,0],[1,0,1],[0,0,0]]
s = Solution()
s.flipAndInvertImage(image)