class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        new_word = ""
        index = word.find(ch)
        if index:
            new_word1 = word[0:index+1]
            new_word += f"{new_word1[::-1]}{word[index+1:]}"
            return new_word