
# @Title: 新21点 (New 21 Game)
# @Author: 2464512446@qq.com
# @Date: 2020-06-03 17:32:51
# @Runtime: 100 ms
# @Memory: 13.9 MB

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        res = [0] * (K+W)
        s = 0
        for i in range(K,K+W):
            res[i] = 1 if i <=N else 0
            s += res[i]  # 超出K值部分的总和
        
        for i in range(K-1,-1,-1):
            res[i] = s/W
            s = s -res[i+W] +res[i]

        return res[0]
