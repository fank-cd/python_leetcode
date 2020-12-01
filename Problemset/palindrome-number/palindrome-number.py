
# @Title: 回文数 (Palindrome Number)
# @Author: 2464512446@qq.com
# @Date: 2020-06-10 12:00:37
# @Runtime: 80 ms
# @Memory: 13.3 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
