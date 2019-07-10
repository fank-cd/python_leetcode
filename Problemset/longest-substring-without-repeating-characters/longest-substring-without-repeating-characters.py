
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: 2464512446@qq.com
# @Date: 2019-07-10 11:51:35
# @Runtime: 68 ms
# @Memory: 13.3 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑窗法
        """
        
        if not s:
            return 0

        left_index = 0
        lookup = set()
        leng = len(s)

        max_len = 0
        cur_len = 0

        for i in range(leng):
            cur_len +=1

            while s[i] in lookup:
                lookup.remove(s[left_index])
                left_index += 1
                cur_len -= 1
            if cur_len >max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len
