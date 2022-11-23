#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。

# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。

# 例如， “ace” 是 “abcde” 的子序列。


# 示例 1:
# 输入: s = "abcde", words = ["a", "bb", "acd", "ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。

# 示例 2:
# 输入: s = "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
# 输出: 2


# 提示:
# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# words[i]和 s 都只由小写字母组成。

# 复习
from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 注意防止TLE
        ptr = defaultdict(list)
        for i, w in enumerate(words):
            ptr[w[0]].append((i, 0))  # 记录当前待批评字符为w[0]的各单词及索引位置

        res = 0
        for c in s:
            p = ptr[c]
            ptr[c] = []  # 清空待匹配c的单词（所有待匹配c的单词，都可以匹配上，且匹配位置后移）
            for i, j in p:
                j += 1
                if j == len(words[i]):
                    res += 1  # 匹配到头
                else:
                    ptr[words[i][j]].append((i, j))

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # 3
    print(solution.numMatchingSubseq("dsahjpjauf", [
          "ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))  # 2
