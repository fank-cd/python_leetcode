
# @Title: 实现 Trie (前缀树) (Implement Trie (Prefix Tree))
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 16:37:55
# @Runtime: 140 ms
# @Memory: 26.2 MB

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node.setdefault(char,{})
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node.setdefault(char,{})
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
 will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
