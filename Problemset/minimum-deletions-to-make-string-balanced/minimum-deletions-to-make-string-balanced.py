
# @Title: 使字符串平衡的最少删除次数 (Minimum Deletions to Make String Balanced)
# @Author: 2464512446@qq.com
# @Date: 2020-11-15 00:39:59
# @Runtime: 848 ms
# @Memory: 22.5 MB

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = [0] * n
        b = [0] * n
        cur = 0
        for i in range(n):
            b[i] = cur
            if s[i] == 'b':
                cur += 1
        cur = 0 
        for i in reversed(range(n)):
            a[i] = cur
            if s[i] == 'a':
                cur += 1
        return min([a[i]+b[i] for i in range(n)])
