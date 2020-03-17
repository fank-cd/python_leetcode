
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 18:08:17
# @Runtime: 84 ms
# @Memory: 12.6 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        
        for i in range(len(prices)-1):
            differ = prices[i+1] - prices[i]
            if differ >0:
                ans +=differ
                
        return ans
            
