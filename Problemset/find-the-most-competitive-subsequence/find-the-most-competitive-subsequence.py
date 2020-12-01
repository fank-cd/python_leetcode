
# @Title: 找出最具竞争力的子序列 (Find the Most Competitive Subsequence)
# @Author: 2464512446@qq.com
# @Date: 2020-11-30 11:03:48
# @Runtime: 192 ms
# @Memory: 23.7 MB

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [nums[0]]
        count =  len(nums) - k
        for item in nums[1:]:
            while stack and item < stack[-1] and count > 0:
                stack.pop()
                count -= 1
            stack.append(item)
        return stack[:k]
