
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 15:40:22
# @Runtime: 32 ms
# @Memory: 10.9 MB

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """
        
        a = s.strip().split(' ')
        if len(a):
            return len(a[-1])
        else:
            return 0
