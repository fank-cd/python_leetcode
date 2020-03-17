
# @Title: 斐波那契数 (Fibonacci Number)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 18:22:52
# @Runtime: 32 ms
# @Memory: 11.7 MB

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # if N ==0 or N ==1:
        #     return N
        # else:
        #     return self.fib(N-1)+ self.fib(N-2)
        

        n, a, b = 0, 0, 1 
        if N == 0:
            return 0
        elif N== 1:
            return 1
        else:
            
            while n < N: 
                a, b = b, a + b 
                n = n + 1
            return a
