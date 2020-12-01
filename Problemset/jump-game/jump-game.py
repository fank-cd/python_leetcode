
# @Title: 跳跃游戏 (Jump Game)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:36:37
# @Runtime: 48 ms
# @Memory: 14.7 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxpos = 0
        for i in range(len(nums)):
            if i > maxpos:
                return False
            maxpos = max(maxpos,i + nums[i])
        return True
