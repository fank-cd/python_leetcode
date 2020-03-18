
# @Title: 斐波那契数列 (斐波那契数列  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-18 16:50:48
# @Runtime: 32 ms
# @Memory: 13.6 MB

class Solution:
    def fib(self, n: int) -> int:
        a,b = 0 ,1

        for _ in range(n):
            a,b = b, a+b
        return a % 1000000007

