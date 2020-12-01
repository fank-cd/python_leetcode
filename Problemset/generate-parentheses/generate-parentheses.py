
# @Title: 括号生成 (Generate Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2020-11-13 15:36:24
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(left,right,p):
            if left:
                helper(left-1,right,p+"(")
            if right > left:
                helper(left,right-1,p+")")
            if not right:
                res.append(p)
        helper(n,n,"")
        return res
