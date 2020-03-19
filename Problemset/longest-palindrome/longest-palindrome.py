
# @Title: 最长回文串 (Longest Palindrome)
# @Author: 2464512446@qq.com
# @Date: 2020-03-19 16:00:15
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution:
    def longestPalindrome(self, s: str) -> int:

        """
        list_str = list(s)
        seen = set(list_str)
        count = 0
        for i in seen:
            if list_str.count(i) %2 !=0:
                count +=1
        if count != 0:
            return len(s) - count +1
        return len(s)

        思想是一样的，但是下面的代码明显更好。
        """
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
