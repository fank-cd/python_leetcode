
# @Title: 有效的括号 (Valid Parentheses)
# @Author: 2464512446@qq.com
# @Date: 2019-03-05 10:40:17
# @Runtime: 36 ms
# @Memory: 10.8 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        left = "({["
        right = ")]}"
        
        
        d = {")":"(","}":"{","]":"["}
        for i in s:
            # print(i)
            if i in d.values():
                l.append(i)
                # print l[:-1]

            elif i in d.keys() and l and d[i]==l[len(l)-1]:
                l.pop()
                # print "OK"
            else:
                return False
            
        return not l
                    
