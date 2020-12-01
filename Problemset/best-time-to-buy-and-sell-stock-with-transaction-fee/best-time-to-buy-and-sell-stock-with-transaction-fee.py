
# @Title: 买卖股票的最佳时机含手续费 (Best Time to Buy and Sell Stock with Transaction Fee)
# @Author: 2464512446@qq.com
# @Date: 2020-11-24 17:10:38
# @Runtime: 1112 ms
# @Memory: 22.5 MB

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        size = len(prices)
        if size < 2:
            return 0
        dp = [[0] *2 for i in range(size)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i] )
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]- fee)
        return dp[-1][1]
