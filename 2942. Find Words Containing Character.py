class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for index, i in enumerate(words):
            if x in i:
                result.append(index)
        return result
