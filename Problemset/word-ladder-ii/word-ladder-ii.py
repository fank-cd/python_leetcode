
# @Title: 单词接龙 II (Word Ladder II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-04 16:23:51
# @Runtime: 164 ms
# @Memory: 19.6 MB

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        successors = defaultdict(set)
        size = len(beginWord)

        res = []
        if len(wordList) == 0 or endWord not in wordList:
            return res
        d = defaultdict(list)
        for i in range(size):
            for word in wordList:
                d[word[:i] + "*" + word[i+1:]].append(word)
        def bfs():
            queue = collections.deque()
            queue.append(beginWord)
            visited = set()
            visited.add(beginWord)
            found = False
            next_level_set = set()
            while queue:
                for i in range(len(queue)):
                    cur_word = queue.popleft()
                    for j in range(size):
                        for next_word in d[cur_word[:j] + "*" +cur_word[j+1:]]:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                if next_word not in next_level_set:
                                    queue.append(next_word)
                                    next_level_set.add(next_word)
                                successors[cur_word].add(next_word)
                if found:
                    break
                visited |= next_level_set
                next_level_set.clear()
            return found
        def dfs(beginWord,path):
            if beginWord == endWord:
                res.append(path[:])
                return 
            if beginWord not in successors:
                return 
            for next_word in successors[beginWord]:
                path.append(next_word)
                dfs(next_word,path)
                path.pop()
        found = bfs()
        # print(successors)
        if not found:
            return res
        path  = [beginWord]
        dfs(beginWord,path)
        return res


