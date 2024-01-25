class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            current = (low + high) // 2

            match guess(current):
                case -1:
                    high = current - 1
                case 1:
                    low = current + 1
                case 0:
                    return current
        return -1