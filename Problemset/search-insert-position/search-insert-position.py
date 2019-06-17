
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: 2464512446@qq.com
# @Date: 2019-03-06 11:30:55
# @Runtime: 28 ms
# @Memory: 11.1 MB

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if i == len(nums)-1:
                    if nums[i] < target:
                        nums.append(target)
                        return i+1
                    if nums[i] > target:
                        nums.insert(0,target)
                        return 0
                    
                elif nums[i] < target and nums[i+1]>target:
                    nums.insert(i+1,target)
                    return i+1
                elif nums[0] > target:
                    nums.insert(0,target)
                    return 0
