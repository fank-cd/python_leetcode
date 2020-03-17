
# @Title: 验证回文串 (Valid Palindrome)
# @Author: 2464512446@qq.com
# @Date: 2019-11-14 11:24:41
# @Runtime: 48 ms
# @Memory: 14.6 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(list(filter(str.isalnum, s))).lower()
        p,q = 0,len(s)-1
        while p<q:
            if s[p] == s[q]:
                p +=1
                q -=1
            else:
                return False
        return True
