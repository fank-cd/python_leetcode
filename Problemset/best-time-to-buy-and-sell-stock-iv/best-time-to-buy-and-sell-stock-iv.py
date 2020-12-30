
# @Title: 买卖股票的最佳时机 IV (Best Time to Buy and Sell Stock IV)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 11:59:13
# @Runtime: 140 ms
# @Memory: 24.4 MB

class Solution:
    def nok_maxprofit(self, prices):
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        size = len(prices)
        if k > size // 2:
            return self.nok_maxprofit(prices)
        dp = [[[0]*2 for i in range(k+1)] for j in range(size)]
        for i in range(k+1):
            dp[0][i][0] = - prices[0]
        for i in range(1, size):
            for j in range(1,k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] - prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] + prices[i])
        return dp[-1][-1][1]
