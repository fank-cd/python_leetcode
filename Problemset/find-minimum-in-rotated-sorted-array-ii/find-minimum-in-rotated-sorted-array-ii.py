
# @Title: 寻找旋转排序数组中的最小值 II (Find Minimum in Rotated Sorted Array II)
# @Author: 2464512446@qq.com
# @Date: 2020-03-19 18:26:54
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0,len(nums)-1

        while low<high:
            mid = (low+high) //2
            if nums[mid] > nums[high]:
                low = mid + 1 
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high = high -1
        return nums[low]
