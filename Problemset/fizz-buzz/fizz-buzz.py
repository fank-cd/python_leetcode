
# @Title: Fizz Buzz (Fizz Buzz)
# @Author: 2464512446@qq.com
# @Date: 2018-12-12 17:15:32
# @Runtime: 52 ms
# @Memory: 8.3 MB

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        """
        l = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                l.append("FizzBuzz")
            elif i%3 == 0:
                l.append("Fizz")
            elif i%5 ==0 :
                l.append("Buzz")
            else:
                l.append(str(i))
                
        return l
