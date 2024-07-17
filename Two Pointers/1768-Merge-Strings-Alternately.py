class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        mergedText = ""
        while (idx1 < len(word1) and idx2 < len(word2)):
            mergedText += (word1[idx1])
            mergedText += (word2[idx2])
            idx1 += 1
            idx2 += 1
        while idx1 < len(word1):
            mergedText += (word1[idx1])
            idx1 += 1
        while idx2 < len(word2):
            mergedText += (word2[idx2])
            idx2 += 1
        return mergedText      

