
# @Title: 和为零的N个唯一整数 (Find N Unique Integers Sum up to Zero)
# @Author: 2464512446@qq.com
# @Date: 2020-01-03 12:05:41
# @Runtime: 36 ms
# @Memory: 12.8 MB

class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        if n % 2 != 0:
            l.append(0)

        index = 1
        while len(l) != n:

            l.append(index)
            l.append(-index)
            index +=1
        
        return l
