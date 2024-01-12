VOWELS = "aeiouAEIOU"
class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)

        start, end = 0, len(s) - 1

        while start < end:
            while start < end and s[start] not in VOWELS:
                start += 1
            while start < end and s[end] not in VOWELS:
                end -=1
            if start < end:
                result[start] = s[end] 
                result[end] = s[start]
                start += 1
                end -= 1
        return "".join(result)

sol = Solution()
print(sol.reverseVowels(s = "hello"))