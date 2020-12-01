
# @Title: 斐波那契数 (Fibonacci Number)
# @Author: 2464512446@qq.com
# @Date: 2020-07-28 18:10:22
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution:
    def fib(self, N: int) -> int:   
        a,b = 0,1
        for i in range(N):
            a,b = b,a+b

        return a
