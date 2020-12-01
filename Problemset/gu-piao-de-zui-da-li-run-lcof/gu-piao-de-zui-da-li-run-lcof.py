
# @Title: 股票的最大利润 (股票的最大利润  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-09-27 16:13:25
# @Runtime: 48 ms
# @Memory: 14.2 MB

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

