#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-25 08:23:38
LastEditors: Thomas Young
LastEditTime: 2020-10-05 08:32:08
'''
#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对
# 位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

# 题目数据保证答案符合 32 位带符号整数范围。

# 示例 1：
# 输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^

# 示例 2：
# 输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t or len(s) < len(t):
            return 0

        ls, lt = len(s), len(t)
        if ls == lt: # s和t长度相同，则判断是否相等
            return int(s == t)
        
        # 记dp(i, j)为s[:i]变化为t[:j]的方法个数, 0 <= i <= ls, 0 <= j <= lt
        # dp(i, j) = dp(i-1, j) if s[i-1] != t[j-1]
        #          = dp(i-1, j-1) + dp(i-1, j) if s[i-1] = t[j-1]
        # dp(i, 0) = 1
        # dp(0, j) = 0 if j != 0
        dp = [0] * (lt + 1)
        dp[0] = 1

        for i in range(ls):
            for j in range(lt - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j+1] = dp[j] + dp[j+1]

        return dp[-1] 

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numDistinct("babgbag", "bag"))
    print(solution.numDistinct("rabbbit", "rabbit"))
