#
# @lc app=leetcode.cn id=2707 lang=python3
#
# [2707] 字符串中的额外字符
#
# 给你一个下标从 0 开始的字符串 s 和一个单词字典 dictionary 。你需要将 s 分割成若干个 互不重叠 的子字符串，每个子字符串都在 dictionary 中出现过。
# s 中可能会有一些 额外的字符 不在任何子字符串中。

# 请你采取最优策略分割 s ，使剩下的字符 最少 。


# 示例 1：
# 输入：s = "leetscode", dictionary = ["leet","code","leetcode"]
# 输出：1
# 解释：将 s 分成两个子字符串：下标从 0 到 3 的 "leet" 和下标从 5 到 8 的 "code" 。只有 1 个字符没有使用（下标为 4），所以我们返回 1 。

# 示例 2：
# 输入：s = "sayhelloworld", dictionary = ["hello","world"]
# 输出：3
# 解释：将 s 分成两个子字符串：下标从 3 到 7 的 "hello" 和下标从 8 到 12 的 "world" 。下标为 0 ，1 和 2 的字符没有使用，所以我们返回 3 。
 

# 提示：
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] 和 s 只包含小写英文字母。
# dictionary 中的单词互不相同。

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
        
    def matchWord(self, s: str, start: int) -> List[int]:
        """
        Returns the possible match word length starting from s[start:]
        """
        res = []
        node = self
        i, j = 0, len(s) - start
        while i < j:
            idx = ord(s[start + i]) - ord('a')
            if node.charArr[idx]:
                node = node.charArr[idx]
            else:
                break
            i += 1
            if node.isEnd:
                res.append(i)

        return res
    
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 构造搜索树
        trie = Trie()
        for w in dictionary:
            trie.insert(w)

        n = len(s)
        unmatchedDict = {}
        unmatched = 0
        for i in range(n):
            unmatched = min(unmatched, unmatchedDict.get(i, i))
            for l in trie.matchWord(s, i): # 从i开始匹配，看有可能匹配上哪些词
                oldVal = unmatchedDict.get(i+l, i+l)
                unmatchedDict[i+l] = min(oldVal, unmatched)
            
            unmatched += 1
            oldVal = unmatchedDict.get(i+1, unmatched)
            unmatchedDict[i+1] = min(oldVal, unmatched)
            
        return unmatchedDict[n]
        

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minExtraChar("leetscode", ["leet","code","leetcode"])) # 1
    print(solution.minExtraChar("sayhelloworld", ["hello","world"])) # 3
