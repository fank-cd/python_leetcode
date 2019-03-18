# coding:utf-8
# 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#

# 首先的是自己的垃圾算法，用set去重后构造一个字典去存取每个nums元素出现的次数
# 最后用zip反转dict，max函数求出最大值，直接返回掉



# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         s = set(nums)
#         d = {_:0 for _ in s}
#         # print d
#         for i in nums:
#             d[i] +=1
#         max_prices = max(zip(d.values(), d.keys()))
#         return max_prices[1]
#         # return max(d.values)


# 这个算法非常精妙，想法是遇到不同元素计量减1，相同元素计量加1，如果cnt等于零，则换下一个元素比较
# 这个思想其实很有意思，首先，算众数求一定有众数，那么众数出现次数一定是最多的
# 遇到相同的则加，不同的则减，这样总能求出最多的，可以多试几个数字感受一下

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ret = 0, 0
        for num in nums:
            if cnt == 0:
                ret = num
            if num != ret:
                cnt -= 1
            else:
                cnt += 1
        return ret