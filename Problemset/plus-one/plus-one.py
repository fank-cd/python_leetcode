
# @Title: 加一 (Plus One)
# @Author: 2464512446@qq.com
# @Date: 2020-11-11 11:51:11
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits or [0]
        last = digits.pop()
        if last == 9:
            return self.plusOne(digits) + [0]
        else:
            return digits + [last+1]
