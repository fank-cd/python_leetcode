
# @Title: 只出现一次的数字 (Single Number)
# @Author: 2464512446@qq.com
# @Date: 2019-11-01 17:29:19
# @Runtime: 100 ms
# @Memory: 13.6 MB

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         d= {}
#         for i in nums:
#             if i not in d:
#                 d[i] =1
#             else:
#                 d[i] +=1
                
#         for k,v in d.items():
#             if v == 1:
#                 return k

# 交换律：a ^ b ^ c <=> a ^ c ^ b

# 任何数于0异或为任何数 0 ^ n => n

# 相同的数异或为0: n ^ n => 0

# var a = [2,3,2,4,4]

# 2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
        a = 0
        for num in nums:
            a = a ^ num
        return a
