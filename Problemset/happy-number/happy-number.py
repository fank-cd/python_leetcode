
# @Title: 快乐数 (Happy Number)
# @Author: 2464512446@qq.com
# @Date: 2019-11-05 17:20:33
# @Runtime: 44 ms
# @Memory: 13.9 MB

class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
            if n == 1:
                return True


