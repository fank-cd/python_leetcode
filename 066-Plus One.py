# coding:utf-8

# 加一

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。



# 不用脑子版

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = ""
        digits = str(digits)
        for i in digits:
            if i in nums:
                s += i

        l = []

        # print s
        s = int(s)
        s += 1
        s = str(s)
        for i in s:
            print i
            l.append(int(i))

        return l