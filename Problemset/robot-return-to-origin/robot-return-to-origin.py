
# @Title: 机器人能否返回原点 (Robot Return to Origin)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 17:12:57
# @Runtime: 32 ms
# @Memory: 11.7 MB

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
