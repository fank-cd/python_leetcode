
# @Title: 独一无二的出现次数 (Unique Number of Occurrences)
# @Author: 2464512446@qq.com
# @Date: 2020-10-28 10:28:54
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d =  Counter(arr)
        res = set()
        for i in d:
            if d[i] not in res:
                res.add(d[i])
            else:
                return False
        return True
