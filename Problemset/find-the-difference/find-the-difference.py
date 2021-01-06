class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        for i in s:
            count[ord(i)- ord('a')] += 1
        for i in t:
            count[ord(i)- ord('a')] -= 1
        for i in range(26):
            if count[i] == -1:
                return chr(ord('a')+i)