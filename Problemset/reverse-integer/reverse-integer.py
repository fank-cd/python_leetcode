
# @Title: 整数反转 (Reverse Integer)
# @Author: 2464512446@qq.com
# @Date: 2019-03-01 17:22:41
# @Runtime: 36 ms
# @Memory: 10.7 MB

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >0:
            a= int(str(x)[::-1])
        elif x < 0:
            a= -int((str(x)[1:])[::-1])
        elif x == 0:
            return 0
        min= -2147483648
        max= 2147483647
        if a > min and a < max:
            return a
        else:
            return 0
