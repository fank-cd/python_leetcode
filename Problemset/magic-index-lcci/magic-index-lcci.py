
# @Title: 魔术索引 (Magic Index LCCI)
# @Author: 2464512446@qq.com
# @Date: 2020-07-31 11:33:06
# @Runtime: 72 ms
# @Memory: 13.8 MB

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for index,i in enumerate(nums):
            if index == i:
                return index

        return -1
