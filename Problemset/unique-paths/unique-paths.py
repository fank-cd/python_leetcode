
# @Title: 不同路径 (Unique Paths)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 11:54:15
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(m)]

        for i in range(1,n):
            for j in range(1,m):
                dp[j] += dp[j-1]
        return dp[-1]
