
# @Title: 括号生成 (Generate Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 14:18:06
# @Runtime: 20 ms
# @Memory: 11.8 MB

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        
        self._dfs(res,n,0,0,"")
        return res
    def _dfs(self,res,n,left,right,temp):
        if left==n and right == n:
            res.append(temp)
            return 
        if left < n:
            self._dfs(res,n,left+1,right,temp+"(")
        if right < left  and right <n :
            self._dfs(res,n,left,right+1,temp+")")


        
