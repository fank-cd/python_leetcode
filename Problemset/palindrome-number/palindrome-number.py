
# @Title: 回文数 (Palindrome Number)
# @Author: 2464512446@qq.com
# @Date: 2019-03-04 10:36:27
# @Runtime: 256 ms
# @Memory: 10.8 MB

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = True
        a = list(str(x))
        if x >=0:
            while flag and len(a) > 1:
                if a.pop() == a.pop(0):
                    pass
                else:
                    flag = False

            if flag:
                return True
            
            else:
                return False
            
        return False
