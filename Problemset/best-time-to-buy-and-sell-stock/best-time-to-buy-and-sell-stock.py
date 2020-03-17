
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 18:17:56
# @Runtime: 84 ms
# @Memory: 12.5 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float("inf")
        
        for i in prices:
            if i < min_price:
                min_price = i
            if i - min_price > max_profit:
                max_profit = i - min_price
                
        return max_profit
