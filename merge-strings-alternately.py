class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = str()
        longer_length = len(word1)
        if longer_length < len(word2):
            longer_length = len(word2)
        
        for i in range(longer_length):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]

        return output