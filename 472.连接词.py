#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
# 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。


# 示例 1：
# 输入：words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
# 输出：["catsdogcats", "dogcatsdog", "ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成
# "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成
# "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。

# 示例 2：
# 输入：words = ["cat", "dog", "catdog"]
# 输出：["catdog"]


# 提示：
# 1 <= words.length <= 10^4
# 0 <= words[i].length <= 1000
# words[i] 仅由小写字母组成
# 0 <= sum(words[i].length) <= 10^5

# Hard

from typing import List
# @lc code=start


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.charArr = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.charArr[idx]:
                node.charArr[idx] = Trie()
            node = node.charArr[idx]
        node.isEnd = True

    def search(self, word: str, start: int) -> bool:
        """
        Returns if the word can be split into part in the trie.
        """
        if start == len(word):
            return True

        node = self
        for i in range(start, len(word)):
            node = node.charArr[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.search(word, i + 1):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 按长度排序
        words.sort(key=len)

        res = []
        trie = Trie()
        for w in words:
            if w:
                if trie.search(w, 0):
                    res.append(w)
                else:
                    trie.insert(w)

        return res
# @lc code=end
