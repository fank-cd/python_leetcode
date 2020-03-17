
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 15:01:45
# @Runtime: 40 ms
# @Memory: 11.6 MB

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        
        for i in range(len(s)):
            if i<len(s) -1 and d[s[i]] < d[s[i+1]]:
                res = res - d[s[i]]
            else:
                res = res+ d[s[i]]
                
        return res
