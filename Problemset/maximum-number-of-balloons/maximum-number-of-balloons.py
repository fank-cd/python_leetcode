
# @Title: “气球” 的最大数量 (Maximum Number of Balloons)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 15:53:32
# @Runtime: 36 ms
# @Memory: 14.7 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        count['l'] //= 2
        count['o'] //= 2

        return min(count['b'],count['a'],count['l'],count['o'],count['n'])
