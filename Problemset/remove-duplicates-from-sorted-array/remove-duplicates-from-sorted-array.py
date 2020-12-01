
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2020-07-06 17:42:38
# @Runtime: 36 ms
# @Memory: 14.5 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j  = 0  # 不相等的元素的下一个位置
        for i in range(1,len(nums)):  # 因为是排序数组，所以可以比较相邻元素
            if nums[j] != nums[i]:  # 遇到不相等的情况，将不相等的元素移到J+1 的位置，
                j += 1
                nums[j] =nums[i]
                
        return j + 1  # +1是因为需要算上第一位元素。
