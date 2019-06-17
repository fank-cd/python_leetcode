
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: 2464512446@qq.com
# @Date: 2019-03-04 15:57:59
# @Runtime: 40 ms
# @Memory: 10.9 MB

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])
        end = 0
        
        while end < minl:
            for i in range(1,len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]
