
# @Title: 数组的相对排序 (Relative Sort Array)
# @Author: 2464512446@qq.com
# @Date: 2020-11-14 21:17:25
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        counter =  Counter(arr1)
        for index, i in enumerate(arr2):
            d[i] = index
        res = [[] for _ in range(len(set(arr2)))]
        for i in d:
            for _ in range(counter[i]):
                res[d[i]].append(i)
        res = [i for j in res for i in j]
        temp = []
        for i in arr1:
            if i not in res:
                temp.append(i)
        res.extend(sorted(temp))
        return res
