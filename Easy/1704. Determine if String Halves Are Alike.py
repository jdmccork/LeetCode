class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s)], s[len(s) + 1:]
        def count(s):
            total = 0
            for char in s:
                if char in "aeiouAEIOU":
                    total += 1
            print(total)
            return total
        return count(a) == count(b)
        
