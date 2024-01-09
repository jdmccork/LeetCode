class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # result = "".join("".join(x) for x in zip(word1, word2)) + word1[min(len(word2), len(word1)):] + word2[min(len(word2), len(word1)):]
        result = ""

        short = min(len(word2), len(word1))
        for i in range(short):
            result += word1[i] + word2[i]
        
        result += word1[short:] + word2[short:]
        
        return result