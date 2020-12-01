
# @Title: 位1的个数 (Number of 1 Bits)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 11:02:00
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            n&=n-1
            count+=1
        return count


