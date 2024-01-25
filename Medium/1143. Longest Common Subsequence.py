class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)) for _ in range(len(text2))]

        for i in range(0, len(text2) + 1):
            for j in range(0, len(text1) + 1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[max(i - 1, 0)][max(j - 1, 0)] + 1

                else:
                    dp[i][j] = max(dp[i][max(j - 1, 0)], dp[max(i - 1, 0)][j])
        return dp[-1][-1]

        # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dp]))

sol = Solution()
# print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
print(sol.longestCommonSubsequence("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))