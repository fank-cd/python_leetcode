
# @Title: 滑动窗口最大值 (Sliding Window Maximum)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 12:01:53
# @Runtime: 368 ms
# @Memory: 26.8 MB

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        for index, i in enumerate(nums):
            if index >= k and index - queue[0] >= k:
                queue.popleft()
            while queue and  nums[queue[-1]] < i:
                queue.pop()
            queue.append(index)
            if index >= k- 1:
                res.append(nums[queue[0]])
        return res
