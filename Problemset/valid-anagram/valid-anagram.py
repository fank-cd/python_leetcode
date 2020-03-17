
# @Title: 有效的字母异位词 (Valid Anagram)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 17:09:44
# @Runtime: 52 ms
# @Memory: 13.2 MB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         if len(s) != len(t):
#             return False
#         d= {}
        
#         for i in s:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] +=1
        
#         for i in t:
#             if i not in d:
#                 return False
#             d[i] -=1
            
#             if d[i] <0:
#                 return False
            
            
#         for v in d.values():
#             if v != 0 :
#                 return False
            
#         return True

        return sorted(s) == sorted(t)
