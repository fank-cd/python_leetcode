
# @Title: 下一个排列 (Next Permutation)
# @Author: 2464512446@qq.com
# @Date: 2020-11-10 15:15:33
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,-1,-1):
            if i==0:
                nums.sort()
            elif nums[i]>nums[i-1]:
                j=len(nums)-1
                while j>=i and nums[j]<=nums[i-1]:
                    j-=1
                temp=nums[i-1]
                nums[i-1]=nums[j]
                nums[j]=temp
                
                nums[i:]=sorted(nums[i:])
                break
