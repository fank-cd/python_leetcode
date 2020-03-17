
# @Title: 分割回文串 (Palindrome Partitioning)
# @Author: 2464512446@qq.com
# @Date: 2019-12-03 11:48:28
# @Runtime: 92 ms
# @Memory: 12 MB

class Solution:
    def partition(self, s):
        res = []
        

        self.helper(s, [],res)
        return res

    def helper(self,s, tmp,res):
        if not s:
            res.append(tmp)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.helper(s[i:], tmp + [s[:i]],res)
