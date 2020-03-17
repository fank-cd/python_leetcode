
# @Title: 反转字符串 (Reverse String)
# @Author: 2464512446@qq.com
# @Date: 2019-10-08 16:18:32
# @Runtime: 180 ms
# @Memory: 18.8 MB

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j = 0,len(s)-1

        while i <j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j -=1
