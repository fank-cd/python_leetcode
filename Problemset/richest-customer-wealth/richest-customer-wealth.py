
# @Title: 最富有客户的资产总量 (Richest Customer Wealth)
# @Author: 2464512446@qq.com
# @Date: 2020-11-29 10:32:42
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = -math.inf
        for i in accounts:
            res = max(res,sum(i))
        return res
