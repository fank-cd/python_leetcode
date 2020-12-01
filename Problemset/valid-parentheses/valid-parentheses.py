
# @Title: 有效的括号 (Valid Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2020-11-13 16:14:41
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "?":"?",
            "[":"]",
            "{":"}",
            "(":")"
        }
        stack= ["?"]
        for i in s:
            if i in d:
                stack.append(i)
            elif d[stack.pop()] != i:
                return False
        return len(stack) == 1
