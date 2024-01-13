class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while (si:=0) < len(s) and (ti:=0) < len(t):
            if t[ti] == s[si]:
                si += 1
                if si == len(s):
                    return True
        return False