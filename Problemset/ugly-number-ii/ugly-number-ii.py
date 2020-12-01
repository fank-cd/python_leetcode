
# @Title: 丑数 II (Ugly Number II)
# @Author: 2464512446@qq.com
# @Date: 2020-09-27 17:46:49
# @Runtime: 180 ms
# @Memory: 13.4 MB

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2=p3=p5=0
        for i in range(n-1):
            
            value = min(nums[p2]*2,nums[p3]*3,nums[p5]*5)

            nums.append(value)

            if nums[p2] *2 == value:
                p2 += 1
            if nums[p3] * 3 == value:
                p3 += 1
            if nums[p5] * 5 == value:
                p5 += 1
        return nums[-1]
