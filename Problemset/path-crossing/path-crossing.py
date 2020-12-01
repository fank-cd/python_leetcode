
# @Title: 判断路径是否相交 (Path Crossing)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 10:05:49
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0),
        }
        x,y = 0,0
        visited = set()
        visited.add((0,0))
        for dire in path:
            # print(directions[dire])
            i,j = directions[dire]
            x,y = x + i, y + j
            # print(x,y)
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
