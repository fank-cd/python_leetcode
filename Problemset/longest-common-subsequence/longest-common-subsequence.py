
# @Title: 最长公共子序列 (Longest Common Subsequence)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:43:36
# @Runtime: 368 ms
# @Memory: 21.1 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
