class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l_word1 = len(word1)
        l_word2 = len(word2)
        iteration = l_word1 if l_word1 > l_word2 else l_word2
        for i in range(iteration):
            if i < l_word1:
                res += word1[i]
            if i < l_word2:
                res += word2[i]
        return res