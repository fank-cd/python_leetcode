
# @Title: 拆炸弹 (Defuse the Bomb)
# @Author: 2464512446@qq.com
# @Date: 2020-11-14 23:03:15
# @Runtime: 48 ms
# @Memory: 13.5 MB

# class ListNode():
#     def __init__(self,val):
#         self.val = val
#         self.next = next
    
class Solution:
    def get_sum(self,i,k,stack,code):
        summ = 0
        count = k // len(code)
        if k > 0:
            for i in range(i+1,i+k+1):
                summ += stack[i]
        elif k < 0:
            k = -k
            for i in range(i+len(code)-1,i-k+len(code)-1,-1):
                summ += stack[i]
                # print(stack,stack[i],i,summ)
        # print(summ)
        if count > 1:
            summ = summ * count
        return summ
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if not code:
            return 0
        stack = code[:]
        stack.extend(code)
        # print(code,stack)
        for i in range(len(code)):
            if k !=0 :
                code[i] = self.get_sum(i,k,stack,code)
            elif k == 0:
                code[i] = 0
        # if k < 0:
        #     return code[::-1]
        return code
