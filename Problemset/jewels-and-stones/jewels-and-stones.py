
# @Title: 宝石与石头 (Jewels and Stones)
# @Author: 2464512446@qq.com
# @Date: 2019-07-16 10:29:21
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
# 执行用时 :44 ms, 在所有 Python3 提交中击败了95.07% 的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了19.55%的用户
        alpha_count = {}
        
        for i in S:
            if i not in alpha_count:
                alpha_count[i] =1
            else:
                alpha_count[i] +=1
        result = 0 
        for i in J:
            if i in alpha_count:
                result += alpha_count[i]

                
        return result
