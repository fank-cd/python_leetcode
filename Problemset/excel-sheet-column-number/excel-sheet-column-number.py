
# @Title: Excel表列序号 (Excel Sheet Column Number)
# @Author: 2464512446@qq.com
# @Date: 2019-10-22 14:51:31
# @Runtime: 16 ms
# @Memory: 11.4 MB

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 想了半天，还说去遍历字符串，直接26进制转10进制就好了
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans
