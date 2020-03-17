
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: 2464512446@qq.com
# @Date: 2019-12-23 18:27:09
# @Runtime: 16 ms
# @Memory: 11.8 MB

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        d ={

            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        res  =[]
        def helper(strr,xdigits):
            if len(xdigits) == 0:
                res.append(strr)
                return 
            else:
                for i in d[xdigits[0]]:
                    ## strr += i
                    helper(strr +i ,xdigits[1:])
                    
        
        helper("",digits)
        # print(res)
        return res
