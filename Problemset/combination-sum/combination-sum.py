
# @Title: 组合总和 (Combination Sum)
# @Author: 2464512446@qq.com
# @Date: 2019-11-21 18:34:04
# @Runtime: 60 ms
# @Memory: 11.4 MB

class Solution(object):
    def combinationSum(self,candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i, tmp_sum, tmp):
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                if tmp_sum + candidates[j] == target:
                    res.append(tmp + [candidates[j]])
                    break
                helper(j, tmp_sum + candidates[j], tmp + [candidates[j]])
        helper(0, 0, [])
        return res


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         size = len(candidates)
#         if size == 0:
#             return []

#         # 剪枝的前提是数组元素排序
#         # 深度深的边不能比深度浅的边还小
#         # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
#         candidates.sort()
#         # 在遍历的过程中记录路径，一般而言它是一个栈
#         path = []
#         res = []
#         # 注意要传入 size ，在 range 中， size 取不到
#         self.__dfs(candidates, 0, size, path, res, target)
#         return res

#     def __dfs(self, candidates, begin, size, path, res, target):
#         # 先写递归终止的情况
#         if target == 0:
#             # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
#             # 或者使用 path.copy()
#             res.append(path[:])

#         for index in range(begin, size):
#             residue = target - candidates[index]
#             # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
#             if residue < 0:
#                 break
#             path.append(candidates[index])
#             # 因为下一层不能比上一层还小，起始索引还从 index 开始
#             self.__dfs(candidates, index, size, path, res, residue)
#             path.pop()

