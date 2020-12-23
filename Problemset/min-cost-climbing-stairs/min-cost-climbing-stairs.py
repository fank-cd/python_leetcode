
# @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
# @Author: 2464512446@qq.com
# @Date: 2020-12-21 15:34:11
# @Runtime: 68 ms
# @Memory: 14.9 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0] * (size+1)
        for i in range(2,size+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[size]
