
# @Title: 数值的整数次方 (数值的整数次方 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-11 17:11:01
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n < 0:
            x, n = 1/x, -n
        res = 1
        while n:
            if n & 1: # 奇数
                res = res * x
            
            x = x * x
            n = n >> 1  #相当于n整除2

        return res 
