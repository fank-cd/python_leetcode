
# @Title: 模拟行走机器人 (Walking Robot Simulation)
# @Author: 2464512446@qq.com
# @Date: 2020-11-04 17:21:30
# @Runtime: 432 ms
# @Memory: 19.1 MB

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = {
            "up":{0:[0, 1], -1:"right", -2:"left"},
            "down":{0:[0, -1], -1:"left", -2:"right"},
            "left": {0:[-1, 0], -1:"up", -2:"down"},
            "right":{0:[1, 0], -1:"down", -2:"up"}
        }
        curdir= "up"
        cord = [0,0]
        res = 0
        obstacles = set(map(tuple,obstacles))

        for cmd in commands:
            if cmd < 0:
                curdir = directions[curdir][cmd]
            else:
                for i in range(cmd):
                    temp_x,temp_y = cord
                    temp_x += directions[curdir][0][0]
                    temp_y += directions[curdir][0][1]
                    if (temp_x,temp_y) in obstacles:
                        break
                    cord = [temp_x,temp_y]
                res = max(res,cord[0]**2 + cord[1]**2)
        return res
