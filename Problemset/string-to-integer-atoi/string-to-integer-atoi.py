
# @Title: 字符串转换整数 (atoi) (String to Integer (atoi))
# @Author: 2464512446@qq.com
# @Date: 2019-03-04 10:19:00
# @Runtime: 60 ms
# @Memory: 10.9 MB

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = '1234567890'
        symbol = '+-'
        result = ''
        
        str = str.strip()
        leng = len(str)
        
        if leng == 0 :
            return 0
        elif leng ==1:
            if str[0] in number:
                return int(str)
            else:
                return 0
        
        if str[0] in number:
            for i in range(leng):
                if str[i] in number:
                    result += str[i]
                else:
                    break
        
        elif str[0] in symbol and str[1] in number:
            result +=str[0]
            for i in range(1,leng):
                if str[i] in number:
                    result +=str[i]
                else:
                    break
        if len(result) == 0:
            return 0
        

        if result[0] in symbol:
            if result[0] == "+":
                if int(result[1:]) > 2147483647:
                    return 2147483647
                else:
                    return int(result[1:])
            elif result[0] == "-":
                if int(result) < -2147483648:
                    return -2147483648
                else:
                    return int(result)
        elif result[0] in number:
            if int(result) > 2147483647:
                return 2147483647
            else:
                return int(result)
