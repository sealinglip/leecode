#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。


# 示例 1:
# 输入: ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "xtfn"。

# 示例 2:
# 输入: ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。

# 示例 3:
# 输入: ["a", "aa", "aaa", "aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。


# 提示：
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] 仅包含小写字母

from typing import List
# @lc code=start
from collections import defaultdict
from functools import reduce
from itertools import product


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)  # key为掩码，value为最长单词长度
        for w in words:
            mask = reduce(lambda x, y: x | (1 << (ord(y) - ord('a'))), w, 0)
            masks[mask] = max(masks[mask], len(w))

        return max([masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0], default=0)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct(
        ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))  # 16
    print(solution.maxProduct(
        ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))  # 4
    print(solution.maxProduct(
        ["a", "aa", "aaa", "aaaa"]))  # 0
