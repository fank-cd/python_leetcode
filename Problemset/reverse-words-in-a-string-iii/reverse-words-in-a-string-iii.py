
# @Title: 反转字符串中的单词 III (Reverse Words in a String III)
# @Author: 2464512446@qq.com
# @Date: 2019-09-29 17:37:49
# @Runtime: 20 ms
# @Memory: 12.8 MB

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(i[::-1] for i in s.split())
