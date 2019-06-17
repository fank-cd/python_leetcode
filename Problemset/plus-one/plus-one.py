
# @Title: 加一 (Plus One)
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 16:54:58
# @Runtime: 32 ms
# @Memory: 10.7 MB

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        nums = ['0','1','2','3','4','5','6','7','8','9']
        s = ""
        digits = str(digits)
        for i in digits:
            if i in nums:
                s += i
            
        
        l = []
        
        
        #print s
        s = int(s)
        s +=1
        s = str(s)
        for i in s:
            print i
            l.append(int(i))
            
        return l
