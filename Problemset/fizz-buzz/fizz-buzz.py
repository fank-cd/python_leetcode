
# @Title: Fizz Buzz (Fizz Buzz)
# @Author: 2464512446@qq.com
# @Date: 2019-11-01 17:48:36
# @Runtime: 24 ms
# @Memory: 12.6 MB

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i %3 ==0  and i %5 == 0:
                res.append("FizzBuzz")
            elif i %3 == 0:
                res.append("Fizz")
            elif i%5 ==0:
                res.append("Buzz")
            else:
                res.append(str(i))
                
        return res
