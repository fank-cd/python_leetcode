
# @Title: 最佳买卖股票时机含冷冻期 (Best Time to Buy and Sell Stock with Cooldown)
# @Author: 2464512446@qq.com
# @Date: 2020-11-19 11:46:51
# @Runtime: 36 ms
# @Memory: 14.1 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        size = len(prices)
        dp = [[0]*3 for i in range(size)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2],dp[i-1][1])
        return max(dp[-1][1],dp[-1][2])
