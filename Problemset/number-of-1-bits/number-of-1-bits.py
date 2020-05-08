
# @Title: 位1的个数 (Number of 1 Bits)
# @Author: 2464512446@qq.com
# @Date: 2020-05-08 18:27:55
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

