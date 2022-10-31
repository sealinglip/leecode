#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。


# 示例 1：
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]

# 示例 2:
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]


# 提示:
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成

from typing import List
# @lc code=start


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            if c.isalpha():
                res = [e + c.lower() for e in res] + [e + c.upper()
                                                      for e in res]
            else:
                res = [e + c for e in res]
        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # ["a1b2", "a1B2", "A1b2", "A1B2"]
    print(solution.letterCasePermutation("a1b2"))
    print(solution.letterCasePermutation("3z4"))  # ["3z4","3Z4"]
