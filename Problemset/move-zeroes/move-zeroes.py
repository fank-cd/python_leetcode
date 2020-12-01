
# @Title: 移动零 (Move Zeroes)
# @Author: 2464512446@qq.com
# @Date: 2020-11-20 16:37:57
# @Runtime: 40 ms
# @Memory: 14.1 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
                
