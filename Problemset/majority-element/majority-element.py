
# @Title: 求众数 (Majority Element)
# @Author: 2464512446@qq.com
# @Date: 2019-03-18 10:55:36
# @Runtime: 40 ms
# @Memory: 11.9 MB

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
