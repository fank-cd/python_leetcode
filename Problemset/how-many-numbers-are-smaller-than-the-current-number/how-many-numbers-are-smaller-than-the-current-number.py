
# @Title: 有多少小于当前数字的数字 (How Many Numbers Are Smaller Than the Current Number)
# @Author: 2464512446@qq.com
# @Date: 2020-10-26 10:51:08
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        res = []

        for i in nums:
            count[i] += 1
        less = []
        temp = 0
        for i in count:
            less.append(temp)
            temp += i
        for i in nums:
            res.append(less[i])
        return res
