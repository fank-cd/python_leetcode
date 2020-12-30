
# @Title: 朋友圈 (Friend Circles)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 15:39:40
# @Runtime: 80 ms
# @Memory: 15 MB

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        size = len(M)
        p = [i for i in range(size)]
        for i in range(size):
            for j in range(size):
                if M[i][j] == 1:
                    self.union(p,i,j)
        return len(set([self.parent(p,i) for i in range(size)]))


    
    def union(self,p,i,j):
        p1 = self.parent(p,i)
        p2 = self.parent(p,j)
        p[p1] = p2

    def parent(self,p,i):
        root = i
        while root != p[root]:
            root = p[root]
        while p[i] != i:
            i,p[i] = p[i],root
        return root 
