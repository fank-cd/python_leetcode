
# @Title: 求1+2+…+n (求1+2+…+n LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-02 18:02:51
# @Runtime: 48 ms
# @Memory: 21 MB

class Solution:
    def sumNums(self, n: int) -> int:
        # 这题对python其实意义不大
        if  n == 1:
            return 1
        return n + self.sumNums(n-1)
