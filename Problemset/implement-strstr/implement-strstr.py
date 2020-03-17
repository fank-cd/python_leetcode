
# @Title: 实现 strStr() (Implement strStr())
# @Author: 2464512446@qq.com
# @Date: 2019-11-19 11:09:09
# @Runtime: 24 ms
# @Memory: 12.1 MB

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if not len(needle):
        #     return 0
        # leng = len(needle)
        # res = 0
        # for i in range(len(haystack)):
        #     if haystack[i:i+leng] == needle:
        #         return i
        # return -1

        # 无赖版本：
        try:
            return haystack.index(needle)
        except:
            return -1
