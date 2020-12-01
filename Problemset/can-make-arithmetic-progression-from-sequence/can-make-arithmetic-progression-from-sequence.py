
# @Title: 判断能否形成等差数列 (Can Make Arithmetic Progression From Sequence)
# @Author: 2464512446@qq.com
# @Date: 2020-07-05 10:50:17
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:  
        if not arr:
            return False
        if len(arr) <2 :
            return arr
        
        arr = sorted(arr)
        # print(arr)
        if (arr[0]+arr[len(arr)-1])*len(arr)/2 == sum(arr):
            return True
        else:
            return False
