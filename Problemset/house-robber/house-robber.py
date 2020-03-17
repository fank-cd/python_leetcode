
# @Title: 打家劫舍 (House Robber)
# @Author: 2464512446@qq.com
# @Date: 2019-11-13 15:57:10
# @Runtime: 12 ms
# @Memory: 11.6 MB

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     递归------>会超时，体现不出动态规划的优越性
    #     if not isinstance(nums,list):
    #         return None
    #     if len(nums) == 0:
    #         return 0
    #     i = len(nums) -1
    #     return self.process(i,nums)

    # def process(self,i,nums):
    #     if i == 0:
    #         return nums[i]
    #     if i == 1:
    #         return max(nums[i],nums[i-1])

    #     return max(self.process(i-2,nums)+nums[i],self.process(i-1,nums))

        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur



