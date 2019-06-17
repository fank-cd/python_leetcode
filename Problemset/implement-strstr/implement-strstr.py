
# @Title: 实现strStr() (Implement strStr())
# @Author: 2464512446@qq.com
# @Date: 2019-03-06 11:09:36
# @Runtime: 464 ms
# @Memory: 12.1 MB

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        """

        
        needle_len = len(needle)
        haystack_len = len(haystack)
        if needle_len ==0 and haystack_len ==0 :
            return 0
        
        if needle_len == 0:
            return 0
        state = False
        
        for i in range(haystack_len):
            if  haystack[i] == needle[0]:
                if haystack[i:i+needle_len] == needle:
                    state = True
                    return i
        

        if not state:
            return -1
