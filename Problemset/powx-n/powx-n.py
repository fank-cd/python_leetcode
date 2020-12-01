
# @Title: Pow(x, n) (Pow(x, n))
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:52:56
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0:
            return x
        if n < 0:
            x,n = 1/x,-n
        res = 1
        while n:
            if n & 1:
                res = x * res
            x = x *x 
            n = n >> 1
        return res
