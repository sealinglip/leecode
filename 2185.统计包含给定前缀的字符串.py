#
# @lc app=leetcode.cn id=2185 lang=python3
#
# [2185] 统计包含给定前缀的字符串
#
# 给你一个字符串数组 words 和一个字符串 pref 。
# 返回 words 中以 pref 作为 前缀 的字符串的数目。
# 字符串 s 的 前缀 就是  s 的任一前导连续字符串。


# 示例 1：
# 输入：words = ["pay", "attention", "practice", "attend"], pref = "at"
# 输出：2
# 解释：以 "at" 作为前缀的字符串有两个，分别是："attention" 和 "attend" 。

# 示例 2：
# 输入：words = ["leetcode", "win", "loops", "success"], pref = "code"
# 输出：0
# 解释：不存在以 "code" 作为前缀的字符串。


# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length, pref.length <= 100
# words[i] 和 pref 由小写英文字母组成

from typing import List
# @lc code=start


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        return sum(1 if w[:pl] == pref else 0 for w in words)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.prefixCount(
        ["pay", "attention", "practice", "attend"], "at"))  # 2
    print(solution.prefixCount(
        ["leetcode", "win", "loops", "success"], "code"))  # 0
