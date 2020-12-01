
# @Title: 跳跃游戏 II (Jump Game II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:37:59
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        maxpos = 0
        end = 0
        for i in range(len(nums)-1):
            maxpos = max(maxpos,nums[i] + i)
            if end == i:
                step += 1
                end = maxpos
        return step
