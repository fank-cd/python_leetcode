
# @Title: 买卖股票的最佳时机 III (Best Time to Buy and Sell Stock III)
# @Author: 2464512446@qq.com
# @Date: 2020-11-19 11:53:58
# @Runtime: 1048 ms
# @Memory: 37.4 MB

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        size = len(prices)
        dp = [[0]*5 for i in range(size)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        for i in range(1,size):
            # dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return max(dp[-1][2],dp[-1][4])
