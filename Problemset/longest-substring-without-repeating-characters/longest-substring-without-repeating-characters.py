
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: 2464512446@qq.com
# @Date: 2019-03-25 11:44:19
# @Runtime: 80 ms
# @Memory: 12.1 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        leng = len(s)
        se = set()
        i, j, ans = 0, 0, 0
        while i < leng and j < leng:
#             print s[j]
            
            if s[j] not in se:
                # print j
                se.add(s[j])
                ans = max(ans,j-i+1)
                j += 1
                
            else:
                # print j
                se.remove(s[i])
                i +=1
                
        return ans
