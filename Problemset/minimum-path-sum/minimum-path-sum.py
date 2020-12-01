
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-10-21 15:14:02
# @Runtime: 48 ms
# @Memory: 14.8 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = grid
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j],dp[i][j-1])
        return dp[i][j]
