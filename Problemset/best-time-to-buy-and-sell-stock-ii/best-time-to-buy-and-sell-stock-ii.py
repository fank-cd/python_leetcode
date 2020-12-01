
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:25:23
# @Runtime: 80 ms
# @Memory: 14.7 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
