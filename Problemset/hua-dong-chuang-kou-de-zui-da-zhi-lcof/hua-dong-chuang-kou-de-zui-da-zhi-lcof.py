
# @Title: 滑动窗口的最大值 (滑动窗口的最大值 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-07-16 11:39:12
# @Runtime: 96 ms
# @Memory: 16.8 MB

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for index,i in enumerate(nums):
            if index >= k and deque[0] <=index -k:
                deque.popleft()
            while deque and nums[deque[-1]] <= i:
                deque.pop()

            deque.append(index)

            if index >= k-1:
                res.append(nums[deque[0]])

        return res
