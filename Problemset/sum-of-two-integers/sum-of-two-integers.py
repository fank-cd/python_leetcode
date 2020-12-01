
# @Title: 两整数之和 (Sum of Two Integers)
# @Author: 2464512446@qq.com
# @Date: 2019-11-05 18:28:42
# @Runtime: 16 ms
# @Memory: 11.5 MB

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # return sum([a, b])

        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
#
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT) 


