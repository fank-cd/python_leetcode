
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: 2464512446@qq.com
# @Date: 2020-11-19 12:09:30
# @Runtime: 32 ms
# @Memory: 13.5 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '1': "",
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ['w', "x", "y", "z"]
        }
        res = []
        size = len(digits)
        if not size:
            return res
        
        def helper(index,path):
            if index == size:
                res.append("".join(path))
                return 
            for i in d[digits[index]]:
                path.append(i)
                helper(index+1,path)
                path.pop()
        helper(0,[])
        return res
