# coding:utf-8

# 最长公共前缀

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
# 说明:
#
# 所有输入只包含小写字母 a-z

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    minl = min([len(x) for x in strs])  # 选择最小的长度值
    end = 0

    while end < minl:
        for i in range(1, len(strs)):  # 这里长度为1-len(strs),但是下面判断的时候为i和i-1，这样是没有问题的
            if strs[i][end] != strs[i - 1][end]:
                return strs[0][:end]  # 不等于则已经找到最长的公共前缀了
        end += 1
    return strs[0][:end]