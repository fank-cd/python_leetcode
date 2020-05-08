
# @Title: 整数拆分 (Integer Break)
# @Author: 2464512446@qq.com
# @Date: 2020-05-07 17:42:17
# @Runtime: 44 ms
# @Memory: 13.8 MB

class Solution:
    def integerBreak(self, n: int) -> int:
        if n<2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = [0 for i in range(n+1)]

        # print(res)
        res[0] = 0
        res[1] = 1
        res[2] = 2
        res[3] = 3

        for i in range(4,n+1):
            for j in range(1,i//2+1):
                temp = res[j]*res[i-j]
                if temp > res[i]:
                    res[i] = temp

        return res[n]

