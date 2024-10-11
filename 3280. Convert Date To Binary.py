class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result = []
        lst = date.split("-")
        for i in lst:
            result.append(bin(int(i))[2:])
        return "-".join(result)


date = "2080-02-29"

cl = Solution()
print(cl.convertDateToBinary(date))