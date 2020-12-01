
# @Title: 多数元素 (Majority Element)
# @Author: 2464512446@qq.com
# @Date: 2020-11-19 12:14:52
# @Runtime: 52 ms
# @Memory: 14.9 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        res = None
        count = 0
        for i in nums:
            if count == 0:
                res = i
            count += 1 if res == i else -1
        return res
