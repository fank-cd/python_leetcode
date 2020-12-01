
# @Title: 调整数组顺序使奇数位于偶数前面 (调整数组顺序使奇数位于偶数前面 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-09 17:50:14
# @Runtime: 48 ms
# @Memory: 17.4 MB

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        p1,p2 = 0,len(nums) -1
        while p1 < p2:
            
            if nums[p1] % 2 == 0:
                # print(p1,p2)
                if nums[p2] % 2 ==1:
                    nums[p1],nums[p2] = nums[p2],nums[p1]
                else:
                    p2 -= 1
            else:
                p1 += 1

        return nums
