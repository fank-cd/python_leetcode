
# @Title: 有效的括号 (Valid Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2019-11-14 14:34:29
# @Runtime: 20 ms
# @Memory: 11.8 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        d = {
            "]":"[",
            ")":"(",
            "}":"{",
        }
        for i in s:
            if i in d:
                top = res.pop() if res else '#'
                if d[i] != top:
                    return False
            else:
                 res.append(i)
        return not res
