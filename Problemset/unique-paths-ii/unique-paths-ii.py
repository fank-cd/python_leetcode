
# @Title: 不同路径 II (Unique Paths II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 11:56:35
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid[0]),len(obstacleGrid)
        dp = [0 for i in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j >= 1:
                    dp[j] += dp[j-1]
        return dp[-1]
