
# @Title: 只出现一次的数字 (Single Number)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 12:17:42
# @Runtime: 28 ms
# @Memory: 12.1 MB

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
