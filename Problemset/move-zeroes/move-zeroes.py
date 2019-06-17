
# @Title: 移动零 (Move Zeroes)
# @Author: 2464512446@qq.com
# @Date: 2019-03-14 11:10:07
# @Runtime: 48 ms
# @Memory: 12 MB

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i <len(nums):
            #print nums
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(len(nums),0)
                i = i-1
                count +=1
                if count == len(nums):
                    break
            i +=1

