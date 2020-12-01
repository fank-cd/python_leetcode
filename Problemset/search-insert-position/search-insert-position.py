
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: 2464512446@qq.com
# @Date: 2020-12-01 16:32:58
# @Runtime: 44 ms
# @Memory: 14 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        res = len(nums)
        while left <= right:
            mid =  left + (right-left)// 2
            # if mid == target:
            #     return mid
            if nums[mid] < target:

                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res
