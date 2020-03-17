
# @Title: 增减字符串匹配 (DI String Match)
# @Author: 2464512446@qq.com
# @Date: 2019-09-28 16:44:11
# @Runtime: 68 ms
# @Memory: 13 MB

class Solution(object):
    def diStringMatch(self, S):
        """ 
        :type S: str
        :rtype: List[int]
        """
        
        min_num,max_num = 0,len(S)
        res = []
        for i in S:
            if i =='I':  #增大
                res.append(min_num)
                min_num +=1
            elif i == 'D':
                res.append(max_num)
                max_num -=1

        return res + [max_num]
