
# @Title: 杨辉三角 (Pascal's Triangle)
# @Author: 2464512446@qq.com
# @Date: 2019-11-01 16:31:50
# @Runtime: 20 ms
# @Memory: 11.4 MB

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            l = [0 for j in range(i+1)]
            l[0] =1
            l[-1] =1
            for j in range(i):
                if l[j] !=1:
                    l[j] = res[i-1][j] + res[i-1][j-1]
            
            res.append(l)
            
        return res
    
