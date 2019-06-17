
# @Title: 验证回文串 (Valid Palindrome)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 11:58:49
# @Runtime: 412 ms
# @Memory: 11.7 MB

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         s = s.lower()
#         letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'
#           ,'w','x','y','z','1','2','3','4','5','6','7','8','9','0']
#         l = []
        
#         for i in s:
#             if i in letter:
#                 l.append(i)
                
#         return l == l[::-1]

        s = s.lower()
        letter = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'
          ,'w','x','y','z','1','2','3','4','5','6','7','8','9','0')
        i = 0
        j = len(s)-1
        
        while i <=j :
            if s[i] in letter and s[j] in letter:
                if s[i] == s[j]:
                    i +=1
                    j -=1
                    
                else:
                    return False
            else:
                
                if s[i] not in letter:
                    i +=1

                if s[j] not in letter:
                    j -=1

        return True
