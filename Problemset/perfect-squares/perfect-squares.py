
# @Title: 完全平方数 (Perfect Squares)
# @Author: 2464512446@qq.com
# @Date: 2019-12-23 17:52:10
# @Runtime: 188 ms
# @Memory: 12.2 MB

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack  = [n]
        level = 0
        visited = set()

        while stack:
            level += 1
            l = len(stack)
            for _ in range(l):
                temp = stack.pop(0)
                for i in range(int(temp**0.5),0,-1):
                    x = temp -i ** 2
                    if x == 0:
                        return level
                    if x not in visited and x >0:
                        stack.append(x)
                        visited.add(x)

        return level

