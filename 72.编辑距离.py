#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-05 22:34:43
LastEditors: Thomas Young
LastEditTime: 2020-10-03 08:06:35
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符

# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse(将 'h' 替换为 'r')
# rorse -> rose(删除 'r')
# rose -> ros(删除 'e')

# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention(删除 't')
# inention -> enention(将 'i' 替换为 'e')
# enention -> exention(将 'n' 替换为 'x')
# exention -> exection(将 'n' 替换为 'c')
# exection -> execution(插入 'u')

# 提示：
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成

# Hard
# 复习
# @lc code=start


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 对于给定的两个字符串，长度记为m和n
        # d(a, b) 定义为两个字符串长度为a(0 <= a <= m)的子串和长度为b(0 <= b <= n)的子串的编辑距离
        # d(a, b) 满足下面条件
        # d(a, b) = min(d(a-1, b-1) + (1 if word1[a-1] != word2[b-1] else 0),
        #               d(a, b-1) + 1, d(a-1, b) + 1), if a > 0 and b > 0
        #         = a + b, if a == 0 or b == 0
        m, n = len(word1), len(word2)

        if m == 0 or n == 0:
            return m + n

        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 状态矩阵
        # 初始化边界
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # 计算所有dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1]
                               [j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0))

        # 如果需要输出具体的变化过程，如下
        # step = []
        # i, j = m, n
        # d = dp[i][j]
        # while d:
        #     if i == 0:
        #         for k in range(j):
        #             step.insert(0, "append char: " + word2[k])
        #         d = 0
        #     elif j == 0:
        #         for k in range(i):
        #             step.insert(0, "delete char: " + word1[k])
        #         d = 0
        #     else:
        #         # 判断走的是哪个递归路径
        #         if d == dp[i][j - 1] + 1:
        #             j -= 1
        #             step.insert(0, "append char: " + word2[j])
        #         elif d == dp[i - 1][j] + 1:
        #             i -= 1
        #             step.insert(0, "delete char: " + word1[i])
        #         else:
        #             j -= 1
        #             i -= 1
        #             if word1[i] != word2[j]:
        #                 step.insert(0, "replace char: from %s to %s" % (word1[i], word2[j]))
        #         d = dp[i][j]
        # print(step)

        return dp[m][n]
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance("horse", "ros"))
    print(solution.minDistance("intention", "execution"))
