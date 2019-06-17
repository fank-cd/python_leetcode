
# @Title: 旋转数组 (Rotate Array)
# @Author: 2464512446@qq.com
# @Date: 2019-03-13 11:39:26
# @Runtime: 236 ms
# @Memory: 11.4 MB

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            nums.pop()
        #return nums
