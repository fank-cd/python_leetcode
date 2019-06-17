
# @Title: 报数 (Count and Say)
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 11:56:26
# @Runtime: 32 ms
# @Memory: 11.2 MB

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import re
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s))
        return s
    
