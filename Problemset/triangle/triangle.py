
# @Title: 三角形最小路径和 (Triangle)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:46:04
# @Runtime: 48 ms
# @Memory: 14 MB

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]
