
# @Title: 单词接龙 (Word Ladder)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 11:04:16
# @Runtime: 160 ms
# @Memory: 17.1 MB

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        queue = collections.deque()
        size = len(beginWord)
        queue.append((beginWord,1))

        for word in wordList:
            for i in range(size):
                d[word[:i] + "*" + word[i+1:]].append(word)
        # print(d)
        visited = set()
        visited.add(beginWord)
        while queue:
            cur_word, step = queue.popleft()
            if cur_word ==  endWord:
                return step
            for i in range(size):
                for word in d[cur_word[:i] + "*" + cur_word[i+1:]]:
                    if word not in visited:
                        queue.append((word,step+1))
                        visited.add(word)
        return 0
