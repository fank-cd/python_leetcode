
# @Title: 移动零 (Move Zeroes)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 16:43:44
# @Runtime: 32 ms
# @Memory: 12.8 MB

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j +=1
        for i in range(j,len(nums)):
            nums[i] = 0
