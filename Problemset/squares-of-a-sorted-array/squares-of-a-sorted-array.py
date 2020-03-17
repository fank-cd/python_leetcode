
# @Title: 有序数组的平方 (Squares of a Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 18:26:07
# @Runtime: 276 ms
# @Memory: 13.7 MB

# 解法1：
# class Solution(object):
#     def sortedSquares(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         return sorted([i*i for i in A])

# 解法2 双指针法
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lenth = len(A)
        for i in range(lenth):
            if A[i] >0:
                break
        minus_num = A[:i][::-1]
        positive_number =A[i:]

        res = []
        i = 0
        j = 0
        while i < len(minus_num) and j < len(positive_number):
            if minus_num[i]**2 < positive_number[j] **2:
                res.append(minus_num[i]**2)
                i +=1
            elif positive_number[j]**2 < minus_num[i] **2:
                res.append(positive_number[j]**2)
                j +=1
            else:
                res.append(positive_number[j]**2)
                res.append(minus_num[i]**2)
                i += 1
                j += 1
            # print(res)
        while i < len(minus_num):
            res.append(minus_num[i]**2)
            i +=1
        while j < len(positive_number):
            res.append(positive_number[j]**2)
            j +=1
        return res
