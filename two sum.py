# coding:utf-8
# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#

# 基本思路是用一个字典来存储遍历过的元素和索引，这样如果(target-nums[i])在arr中，则两数之和成立，通过字典返回索引

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    arr = {}
    length = len(nums)
    for i in range(length):
        if (target - nums[i]) in arr:
            return [arr[target - nums[i]], i]
        print arr
        arr[nums[i]] = i


print twoSum([2,7,11,15],9)