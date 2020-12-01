
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 17:14:02
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif nums[0] <= num:
                if nums[0] <= target < num:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if num < target <= nums[-1]:
                    left = mid +1
                else:
                    right = mid - 1
        return -1
