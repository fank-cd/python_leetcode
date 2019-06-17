
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 11:37:44
# @Runtime: 28 ms
# @Memory: 11.1 MB

class Solution(object):
    
    
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 2**31
        # maxprice = 0
        
        maxprofit = 0
        for i in prices:
            if i < minprice:
                minprice = i
            elif i - minprice > maxprofit:
                    maxprofit = i - minprice
            
        return maxprofit
                
