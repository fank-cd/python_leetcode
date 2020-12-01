
# @Title: 表示数值的字符串 (表示数值的字符串 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-03 17:37:25
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
