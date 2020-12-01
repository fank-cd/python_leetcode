
# @Title: 根据数字二进制下 1 的数目排序 (Sort Integers by The Number of 1 Bits)
# @Author: 2464512446@qq.com
# @Date: 2020-11-06 12:26:16
# @Runtime: 52 ms
# @Memory: 13.5 MB

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key = lambda x : (bin(x).count("1"),x))
