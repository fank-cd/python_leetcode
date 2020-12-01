
# @Title: 猜数字 (Guess Numbers)
# @Author: 2464512446@qq.com
# @Date: 2019-09-28 16:36:28
# @Runtime: 24 ms
# @Memory: 11.4 MB

class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        if not isinstance(guess,list) or not isinstance(answer,list) or len(guess) != len(answer):
            return None
        
        count = 0
        for i in range(3):
            if guess[i] == answer[i]:
                count +=1

        return count
        
