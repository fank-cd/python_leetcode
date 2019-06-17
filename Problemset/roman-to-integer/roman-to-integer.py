
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: 2464512446@qq.com
# @Date: 2019-03-04 15:56:53
# @Runtime: 112 ms
# @Memory: 10.7 MB

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rotonum = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        #half = ["IV","IX","XL","XC","CD","CM"]
        half = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        half_alpha = ["I","X","C"]
        #for i in range(len(s)):
        i = 0
        leng = len(s)
        sum = 0
        while i < leng:
            if s[i] in half_alpha and i+1 <leng:
                if s[i:i+2] in half.keys():
                    sum += half[s[i:i+2]]
                    i += 2
                    continue
            sum += rotonum[s[i]]
            i += 1
            
        return sum
