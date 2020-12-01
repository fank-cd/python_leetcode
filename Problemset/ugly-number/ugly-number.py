
# @Title: 丑数 (Ugly Number)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 12:34:10
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while num % 5 == 0:
            num = num /5
        while num % 3 == 0:
            num = num /3
        while num % 2 == 0:
            num = num /2
        return num == 1
