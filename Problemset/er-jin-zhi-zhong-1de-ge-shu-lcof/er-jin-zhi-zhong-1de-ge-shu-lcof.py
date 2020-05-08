
# @Title: 二进制中1的个数 (二进制中1的个数 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-08 18:31:09
# @Runtime: 52 ms
# @Memory: 13.5 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

# 牛逼算法
# 如果我们把一个数减去1。如果这个整数不等于0，那么该整数的二进制表示中至少有一位是1。
# 先假设最右边一位是1，减1后，最后一位变成0，而其他所有位保持不变。
# 如果最后一位不是1而是0。如果该整数的二进制表示中最右边的1位于第m位，那么减去1时
# 第m位由1变成0，而第m位之后所有0变成1，整数中第m位之前的所有位数都保持不变。
# 接下来我们把一个整数和它减去1的结果做位与运算。相当于把它最右边的1变成0

# 人话：就是不断把最右为变成0，然后不断+1
# 这个解法超级秀
#
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             res += 1
#             n &= n - 1
#         return res


