
# @Title: 旋转数组 (Rotate Array)
# @Author: 2464512446@qq.com
# @Date: 2019-11-15 18:23:55
# @Runtime: 64 ms
# @Memory: 12.3 MB

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k %= n
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

       
        n=len(nums)
        k=k%n
        p1 = nums[:n-k]
        p2 = nums[n-k:n]
        # print(p1,p2)
        nums[:] = p1[::-1] + p2[::-1]
        nums[:] = nums[::-1]
# 第一段，对应数组下标范围[0,n−k−1]
# 第二段，对应数组下标范围[n−k,n−1]


