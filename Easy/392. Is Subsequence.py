class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        return si == len(s)
