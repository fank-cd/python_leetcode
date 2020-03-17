
# @Title: 3的幂 (Power of Three)
# @Author: 2464512446@qq.com
# @Date: 2019-11-12 11:26:18
# @Runtime: 104 ms
# @Memory: 11.7 MB

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        elif n ==1:
            return True
        return self.isPowerOfThree(n/3) and n %3 ==0
