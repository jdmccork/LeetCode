class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recurs(s, p):
            if s == "" and len(p) == 0:
                return True
            if p == "" and s != "":
                return False
            
            found = False
            if not (len(p) > 1 and p[1] == '*') and s != "" and (s[0] == p[0] or p[0] == "."):
                found = recurs(s[1:], p[1:])
            else:
                if len(p) >= 2 and p[1] == "*":
                    found = recurs(s, p[2:])
                    j = 0
                    while not found and (j == len(s) or (j < len(s) and (s[j] == p[0] or p[0] == "."))):
                        found = recurs(s[j + 1:], p[2:])
                        j += 1

            return found
        return recurs(s, p)

sol = Solution()

print(sol.isMatch(s = "aa", p = "a") == False)
print(sol.isMatch(s = "aa", p = "a*") == True)
print(sol.isMatch(s = "ab", p = ".*") == True)
print(sol.isMatch(s = "aaaa", p = "a*.") == True)
print(sol.isMatch(s = "aab", p = "c*a*b") == True)
print(sol.isMatch(s = "mississippi", p = "mis*is*ip*.") == True)
print(sol.isMatch(s = "missi", p = "mis*i") == True)
print(sol.isMatch(s = "mississippi", p = "mis*is*p*.") == False)
print(sol.isMatch(s = "a", p = "ab*") == True)
print(sol.isMatch(s = "ab", p = ".*c") == False)
print(sol.isMatch(s = "a", p = ".*..a*") == False)