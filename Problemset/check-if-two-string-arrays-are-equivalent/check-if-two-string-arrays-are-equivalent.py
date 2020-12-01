
# @Title: 检查两个字符串数组是否相等 (Check If Two String Arrays are Equivalent)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 11:29:28
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
