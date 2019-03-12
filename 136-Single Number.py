# coding:utf-8

# 只出现一次的数字

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
#
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
#
# 此题是考察位运算的异或运算符
# 重点是
# 交换律：a ^ b ^ c <= > a ^ c ^ b
#
# 任何数于0异或为任何数
# 0 ^ n = > n
#
# 相同的数异或为0: n ^ n = > 0

# 暴力法直接解决

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums = sorted(nums)
#         i=0
#         #print len( nums)
#         #print nums[20000]
#
#         #print nums[19990:20001]
#         #print nums[20000]
#         while i <len(nums):
#             if i == len(nums)-1:
#                 return nums[i]
#             if nums[i] == nums[i+1]:
#                 i += 2
#                 #break
#             else:
#                 return nums[i]
#

# 二进制位运算 异或运算


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a

