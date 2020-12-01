
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: 2464512446@qq.com
# @Date: 2020-11-19 11:58:18
# @Runtime: 52 ms
# @Memory: 14.3 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        res = 0
        for price in prices:
            minprice = min(minprice,price)
            res = max(res,price - minprice)
        return res
