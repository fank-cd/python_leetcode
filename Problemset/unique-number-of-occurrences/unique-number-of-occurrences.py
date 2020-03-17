
# @Title: 独一无二的出现次数 (Unique Number of Occurrences)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 14:50:17
# @Runtime: 24 ms
# @Memory: 11.9 MB

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        

        res = set()
        for value in d.values():
            if value not in res:
                res.add(value)
            else:
                return False
        
        return True
