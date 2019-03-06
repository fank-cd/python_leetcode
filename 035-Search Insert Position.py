# coding:utf-8

# 搜索插入位置

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#

# 解题思路：毫无美感的笨方法

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
            if i == len(nums) - 1:
                if nums[i] < target:
                    nums.append(target)
                    return i + 1
                if nums[i] > target:
                    nums.insert(0, target)
                    return 0

            elif nums[i] < target and nums[i + 1] > target:
                nums.insert(i + 1, target)
                return i + 1
            elif nums[0] > target:
                nums.insert(0, target)
                return 0