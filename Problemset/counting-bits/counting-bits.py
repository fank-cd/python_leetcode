
# @Title: 比特位计数 (Counting Bits)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 11:08:21
# @Runtime: 92 ms
# @Memory: 20.1 MB

class Solution:
    def countBits(self, num: int) -> List[int]:

        ret = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                ret.append(ret[i//2])
            else:
                ret.append(ret[i-1]+1)
        return ret
