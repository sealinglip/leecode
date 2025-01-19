# 给你一个字符串数组 words 和一个字符串 target。
# 如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。
# 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。


# 示例 1：
# 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
# 输出： 3
# 解释：
# target 字符串可以通过连接以下有效字符串形成：
# words[1] 的长度为 2 的前缀，即 "aa"。
# words[2] 的长度为 3 的前缀，即 "bcd"。
# words[0] 的长度为 3 的前缀，即 "abc"。

# 示例 2：
# 输入： words = ["abababab","ab"], target = "ababaababa"
# 输出： 2
# 解释：
# target 字符串可以通过连接以下有效字符串形成：
# words[0] 的长度为 5 的前缀，即 "ababa"。
# words[0] 的长度为 5 的前缀，即 "ababa"。

# 示例 3：
# 输入： words = ["abcdef"], target = "xyz"
# 输出： -1

# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 5 * 10^3
# 输入确保 sum(words[i].length) <= 10^5。
# words[i] 只包含小写英文字母。
# 1 <= target.length <= 5 * 10^3
# target 只包含小写英文字母。

from math import inf
from typing import List

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

    def matchPrefix(self, word: str) -> int:
        """
        Returns the length of matched prefix
        """
        node = self
        matched = 0
        for c in word:
            idx = ord(c) - ord('a')
            if node.charArr[idx]:
                node = node.charArr[idx]
                matched += 1
            else:
                break
        return matched
    
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # 构造搜索树
        trie = Trie()
        for w in words:
            trie.insert(w)

        n = len(target)
        # 记dp[i]为target[:i]需要连接的最少字符串数
        dp = [inf] * (n+1)
        dp[0] = 0
        i = 0
        while i < n:
            matched = trie.matchPrefix(target[i:])
            if matched > 0:
                for j in range(matched):
                    dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)
            elif dp[i+1] == inf:
                break
            i += 1

        return -1 if dp[-1] == inf else dp[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.minValidStrings(["abc","aaaaa","bcdef"], "aabcdabc")) # 3
    print(solution.minValidStrings(["abababab","ab"], "ababaababa")) # 2
    print(solution.minValidStrings(["abcdef"], "xyz")) # -1

