
# @Title: 旋转数组 (Rotate Array)
# @Author: 2464512446@qq.com
# @Date: 2020-11-10 16:07:36
# @Runtime: 36 ms
# @Memory: 13.8 MB

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 

        def reverse(t,s):
            while t < s:
                nums[s],nums[t] = nums[t], nums[s]
                t += 1
                s -= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
