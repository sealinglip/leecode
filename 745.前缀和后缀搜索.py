#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#
# 设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。

# 实现 WordFilter 类：

# WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
# f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 - 1 。


# 示例：

# 输入
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# 输出
# [null, 0]
# 解释
# WordFilter wordFilter = new WordFilter(["apple"])
# wordFilter.f("a", "e")
# // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。

# 提示：

# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 7
# 1 <= pref.length, suff.length <= 7
# words[i]、pref 和 suff 仅由小写英文字母组成
# 最多对函数 f 执行 10^4 次调用

from typing import List, Set, Dict
# @lc code=start


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefTrie = {}
        self.suffTrie = {}
        # 因为只需要返回最大索引，这里需要去重
        d = {w: i for i, w in enumerate(words)}
        for w, i in d.items():
            self.buildDict(i, w, self.prefTrie)
            self.buildDict(i, w[::-1], self.suffTrie)

    def buildDict(self, idx: int, word: str, trie: Dict) -> None:
        cur = trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
            if '#' not in cur:
                cur['#'] = set()
            cur['#'].add(idx)

    def search(self, word: str, trie: Dict) -> Set:
        cur = trie
        for c in word:
            if c not in cur:
                return None
            cur = cur[c]
        return cur.get('#', None)

    def f(self, pref: str, suff: str) -> int:
        res1 = self.search(pref, self.prefTrie)
        res2 = self.search(suff[::-1], self.suffTrie)

        if res1 and res2:
            res = res1.intersection(res2)  # 求交集
            if res:
                return max(res)

        return -1

        # Your WordFilter object will be instantiated and called as such:
        # obj = WordFilter(words)
        # param_1 = obj.f(pref,suff)
        # @lc code=end
if __name__ == "__main__":
    wordFilter = WordFilter(["f"] * 10000)
    print(wordFilter.f("f", "f"))

    wordFilter = WordFilter(["abbba", "abba"])
    print(wordFilter.f("ab", "ba"))

    wordFilter = WordFilter(["apple"])
    print(wordFilter.f("a", "e"))
