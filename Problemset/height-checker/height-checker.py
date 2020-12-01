
# @Title: 高度检查器 (Height Checker)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 17:20:04
# @Runtime: 28 ms
# @Memory: 11.4 MB

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(h1!=h2 for h1,h2 in zip(heights,sorted(heights)))
