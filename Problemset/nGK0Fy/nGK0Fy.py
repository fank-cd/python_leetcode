
# @Title: 速算机器人 (速算机器人)
# @Author: 2464512446@qq.com
# @Date: 2020-10-21 15:26:04
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def calculate(self, s: str) -> int:
        x,y = 1,0
        for i in s:
            if i == "A":
                x = 2 * x + y 
            elif i == "B":
                y = 2 * y + x
        
        return x+y
