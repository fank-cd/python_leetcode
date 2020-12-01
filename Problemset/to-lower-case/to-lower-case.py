
# @Title: 转换成小写字母 (To Lower Case)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 15:28:16
# @Runtime: 20 ms
# @Memory: 11.5 MB

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for i in str:
            if not i.islower() and i.isalpha():  # i为大写字母
                i = chr(ord(i)+32)
            res += i
            
        return res
