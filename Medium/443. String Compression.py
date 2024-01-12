class Solution:
    def compress(self, chars: [str]) -> int:
        currentChar = chars[0]
        count = 1
        i = 1

        while i < len(chars):
            if currentChar == chars[i]:
                count += 1
                chars.pop(i)
            else:
                if count > 1:
                    for index, char in enumerate(str(count)):
                        chars.insert(i + index, char)
                    i += len(str(count))
                count = 1
                if i < len(chars):
                    currentChar = chars[i]
                    i += 1
        if count > 1:
            for index, char in enumerate(str(count)):
                    chars.insert(i + index, char)
        return len(chars)
    
sol = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","b","b"]
sol.compress(chars)
print(chars)