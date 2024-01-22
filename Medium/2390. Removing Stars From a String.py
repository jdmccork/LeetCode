class Solution:
    def removeStars(self, s: str) -> str:
        reversedString = s[::-1]
        stack = []
        sol = ""

        for char in reversedString:
            if char == "*":
                stack.append(char)
            elif len(stack) != 0:
                stack.pop()
                continue
            else:
                sol += char
        return sol[::-1]