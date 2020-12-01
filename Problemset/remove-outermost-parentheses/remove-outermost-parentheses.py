
# @Title: 删除最外层的括号 (Remove Outermost Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2020-07-14 17:05:47
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ''
        for i in S:
            if i == '(':
                stack.append(i)
                if len(stack) > 1:
                    result += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    result += ')'
        return result

