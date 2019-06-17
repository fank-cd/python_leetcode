
# @Title: 计数质数 (Count Primes)
# @Author: 2464512446@qq.com
# @Date: 2019-03-13 12:02:49
# @Runtime: 484 ms
# @Memory: 81.7 MB

class Solution(object):
    
    
    def countPrimes(self, n):
        if n < 3: 
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0 
        for i in range(2, n): 
            if prime[i] == 1: 
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i]) 
        return sum(prime)

