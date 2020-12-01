
# @Title: 两数之和 (Two Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-11-20 16:48:40
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, i in enumerate(nums):
            num = target - i
            if num not in d:
                d[i] = index
            else:
                return [d[num],index]
