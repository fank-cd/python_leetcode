
# @Title: 分发糖果 (Candy)
# @Author: 2464512446@qq.com
# @Date: 2020-12-24 15:40:09
# @Runtime: 92 ms
# @Memory: 16.7 MB

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
            else:
                candy[i] = 1
            
        candy_right = 0
        res = 0
        for i in range(n-1,-1,-1):
            if i < n - 1 and ratings[i] > ratings[i+1]:
                candy_right +=1
            else:
                candy_right = 1
            res += max(candy_right,candy[i])
        return res
