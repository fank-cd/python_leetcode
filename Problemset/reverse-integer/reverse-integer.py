
# @Title: 整数反转 (Reverse Integer)
# @Author: 2464512446@qq.com
# @Date: 2019-11-19 14:38:37
# @Runtime: 28 ms
# @Memory: 11.7 MB

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        s = str(x)
        if not s:
            return 
        if x == 0:
            return 0
        if s[0] == "-":
            s = s[1:]
            flag = True
        res = ""
        if flag:
            res  += "-"

        s = s[::-1]
        for i in s:
            if (i==0 and (res =="" or res == "-")) or i !=0:
                res +=i
        if int(res) > -2**31 and int(res) < 2 **31:
                return int(res)
        return 0
                

