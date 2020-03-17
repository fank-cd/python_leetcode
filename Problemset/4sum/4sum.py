
# @Title: 四数之和 (4Sum)
# @Author: 2464512446@qq.com
# @Date: 2019-12-17 11:07:53
# @Runtime: 172 ms
# @Memory: 16.2 MB

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 两两之间当做两数之和来处理
        d = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d.setdefault(nums[i] + nums[j], []).append((i, j))

        result = set()
        ## print(d)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for a, b in d.get(target - nums[i] - nums[j], []):  # 两数之和经典步骤
                    # target-nums[i] -nums[j] 能存在d中，证明存在nums[i] + nums[j] + d中某个key = target
                    # 因为d中key也是nums[i] + nums[j] 所以条件存在
                    # 因为可能有重复的选项，所以记录索引去去重
                    temp = {i, j, a, b}  # 去重
                    if len(temp) == 4:
                        result.add(tuple(sorted(nums[t] for t in temp)))  # 去重

        return result

