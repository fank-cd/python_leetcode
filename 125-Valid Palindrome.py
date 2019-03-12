# coding:utf-8

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false

# 分别用了双指针和直接遍历
# 但是都不太理想效果。。
# 没啥好说的， 双指针就是一个从前遍历，一个从后面遍历，遇到一样的就前进，不一样的就false，不是字母数字的就跳过


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
        letter = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
        , 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] in letter and s[j] in letter:
                if s[i] == s[j]:
                    i += 1
                    j -= 1

                else:
                    return False
            else:

                if s[i] not in letter:
                    i += 1

                if s[j] not in letter:
                    j -= 1

        return True