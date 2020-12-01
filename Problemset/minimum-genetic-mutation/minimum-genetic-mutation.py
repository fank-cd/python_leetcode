
# @Title: 最小基因变化 (Minimum Genetic Mutation)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 10:59:11
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        genes = ['A', 'C', 'G', 'T']
        queue = collections.deque()
        queue.append((start,0))
        size = len(end)
        while queue:
            cur_gene,step = queue.popleft()
            if cur_gene == end:
                return step
            for i in range(size):
                for gene in genes:
                    new_gene = cur_gene[:i] + gene + cur_gene[i+1:]
                    if new_gene in bank:
                        queue.append((new_gene,step+1))
                        bank.remove(new_gene)
        return -1
