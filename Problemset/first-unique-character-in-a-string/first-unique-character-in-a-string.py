
# @Title: 字符串中的第一个唯一字符 (First Unique Character in a String)
# @Author: 2464512446@qq.com
# @Date: 2019-11-14 11:56:12
# @Runtime: 248 ms
# @Memory: 12.1 MB

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # d = {}

        # for i in s:
        #     if i not in d :
        #         d[i] =1
        #     else:
        #         d[i] +=1

        # for i in range(len(s)):
        #     if d[s[i]] == 1:
        #         return i
        # return -1
        count = collections.Counter(s)
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1       
        return -1


