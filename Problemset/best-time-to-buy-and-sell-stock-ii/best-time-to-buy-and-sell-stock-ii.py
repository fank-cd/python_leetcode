
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 11:39:49
# @Runtime: 32 ms
# @Memory: 12 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        money = 0
        length = len(prices)
        
        for i in range(length-1):
            if prices[i]<prices[i+1]:
                # buy
                money +=prices[i+1]-prices[i]
        return money
