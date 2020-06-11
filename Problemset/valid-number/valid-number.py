
# @Title: 有效数字 (Valid Number)
# @Author: 2464512446@qq.com
# @Date: 2020-06-03 17:46:00
# @Runtime: 44 ms
# @Memory: 13.7 MB

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
