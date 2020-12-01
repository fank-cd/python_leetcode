
# @Title: 猜数字游戏 (Bulls and Cows)
# @Author: 2464512446@qq.com
# @Date: 2020-07-12 00:08:28
# @Runtime: 36 ms
# @Memory: 13.5 MB

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull,cow=0,0
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                bull+=1
                cow-=1
        l = set(guess) & set(secret)
        for i in l:
            cow+=min(secret.count(i),guess.count(i))
        return '{0}A{1}B'.format(str(bull),str(cow))
