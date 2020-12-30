
# @Title: 分发饼干 (Assign Cookies)
# @Author: 2464512446@qq.com
# @Date: 2020-12-25 10:05:16
# @Runtime: 72 ms
# @Memory: 16 MB

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi,si = 0, 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi
