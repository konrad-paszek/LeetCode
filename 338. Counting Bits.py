class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            counter = 0
            while i:
                if i & 1:
                    counter += 1
                i >>= 1
            result.append(counter)
        return result
