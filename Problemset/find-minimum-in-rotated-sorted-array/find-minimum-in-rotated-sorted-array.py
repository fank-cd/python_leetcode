
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 16:02:13
# @Runtime: 32 ms
# @Memory: 15 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[0] <= nums[mid]:
                left = mid +1
            else:
                right = mid -1
        return False
