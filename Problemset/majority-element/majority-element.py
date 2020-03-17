
# @Title: 多数元素 (Majority Element)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 14:56:10
# @Runtime: 156 ms
# @Memory: 13.2 MB

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
