
# @Title: 加一 (Plus One)
# @Author: 2464512446@qq.com
# @Date: 2019-11-13 17:31:10
# @Runtime: 20 ms
# @Memory: 11.7 MB

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        res = []
        # num+= str(i)+num for i in digits
        for i in digits:
            num += str(i)
        num = str(int(num)+1)
        for i in num:
            res.append(int(i))

        return res
