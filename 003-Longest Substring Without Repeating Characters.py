# coding:utf-8
# 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#

# 最开始的想法就是直接暴力法
# 后来想了下试了最大子序和的办法
# 但是最大子序和那里是有序的序列，解法不是最优解的

# 最后用的是滑动窗法，简单易懂

# 大概思想是 如果s[i:j]确定是没有重复字符串的字串，那么不必再去算s[i:j+1]
# 而是可以直接看s[j+1]有没有字串在s[i:j]中
# 用set来保存出现过的字串，ans来保存结果

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        leng = len(s)
        se = set()
        i, j, ans = 0, 0, 0
        while i < leng and j < leng:
            if s[j] not in se:
                # print j
                se.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                # print j
                se.remove(s[i])
                i += 1
        return ans