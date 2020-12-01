
# @Title: 字符的最短距离 (Shortest Distance to a Character)
# @Author: 2464512446@qq.com
# @Date: 2019-10-22 14:50:56
# @Runtime: 32 ms
# @Memory: 11.4 MB

class Solution(object):
    """
    本质是以字符C为原点，计算每个字符离字符C有多远。左右各计算一次，取最小值
    """
    def shortestToChar(self, S, C):
        prev = float('-inf')  # 负无穷
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')  # 正无穷
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

