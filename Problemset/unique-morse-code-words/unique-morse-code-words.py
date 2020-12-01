
# @Title: 唯一摩尔斯密码词 (Unique Morse Code Words)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 16:56:31
# @Runtime: 24 ms
# @Memory: 11.5 MB

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {
            'a': '.-',
            'b': '-...',  
            'c': '-.-.',  
            'd': '-..',  
            'e': '.',  
            'f': '..-.',  
            'g': '--.',  
            'h': '....', 
            'i': '..',  
            'j': '.---',  
            'k': '-.-',  
            'l': '.-..',  
            'm': '--',  
            'n': '-.', 
            'o': '---',  
            'p': '.--.',  
            'q': '--.-',  
            'r': '.-.',  
            's': '...',  
            't': '-', 
            'u': '..-',  
            'v': '...-',  
            'w': '.--',  
            'x': '-..-',  
            'y': '-.--',  
            'z': '--..'
        }
        s= set()
    
        for i in words:
            str = ""
            for j in i:
                str +=d[j]
            s.add(str)
            
        return len(s)
