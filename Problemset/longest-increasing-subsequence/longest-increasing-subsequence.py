
# @Title: 最长递增子序列 (Longest Increasing Subsequence)
# @Author: 2464512446@qq.com
# @Date: 2020-12-01 15:05:34
# @Runtime: 60 ms
# @Memory: 13.6 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d= []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l,r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l+r) // 2
                    if d[mid] >=n:
                        loc = mid
                        r = mid -1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d) 
