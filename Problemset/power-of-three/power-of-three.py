
# @Title: 3的幂 (Power of Three)
# @Author: 2464512446@qq.com
# @Date: 2018-12-14 10:14:38
# @Runtime: 176 ms
# @Memory: 7 MB

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 3:
            return True
        elif n % 3 !=0:
            return False
        elif n == 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
        
