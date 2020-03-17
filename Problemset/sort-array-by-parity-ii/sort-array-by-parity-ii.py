
# @Title: 按奇偶排序数组 II (Sort Array By Parity II)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 18:29:44
# @Runtime: 208 ms
# @Memory: 14 MB

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]
