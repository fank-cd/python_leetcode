
# @Title: 翻转图像 (Flipping an Image)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 16:15:55
# @Runtime: 48 ms
# @Memory: 11.7 MB

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[j ^ 1 for j in i[::-1]] for i in A]
