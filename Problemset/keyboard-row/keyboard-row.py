
# @Title: 键盘行 (Keyboard Row)
# @Author: 2464512446@qq.com
# @Date: 2019-10-08 16:59:59
# @Runtime: 24 ms
# @Memory: 11.5 MB

class Solution(object):
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
               
            
        return res
