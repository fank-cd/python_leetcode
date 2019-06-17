
# @Title: x 的平方根 (Sqrt(x))
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 17:28:39
# @Runtime: 44 ms
# @Memory: 10.9 MB

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x <=1:
            return x
        lo,hi = 0,x
        guess = 0
        
        while lo <hi:
            
            
            # print lo,hi
            if guess == (lo+hi)/2:
                return guess
            guess = (lo+hi)/2 
            
            if guess**2 == x:
                return guess
            elif guess**2 <x:
                lo =guess
                
            else:
                hi = guess
                
        return guess
