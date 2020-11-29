#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-01 23:04:04
LastEditors: Thomas Young
LastEditTime: 2020-10-01 23:54:13
'''
# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含
# 小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。出于美观整齐的考虑，小扣想要将收藏集中树叶的
# 排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换
# 成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

# 示例 1：
# 输入：leaves = "rrryyyrryyyrr"
# 输出：2
# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

# 示例 2：
# 输入：leaves = "ryr"
# 输出：0
# 解释：已符合要求，不需要额外操作

# 提示：
# 3 <= leaves.length <= 10 ^ 5
# leaves 中只包含字符 'r' 和字符 'y'


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        if not leaves:
            return 0
        
        # 规划如何翻转
        # 以0，1，2分别代表ryr的三部分
        # dp(idx)共三个元素，分别代表位置idx的🍃要处于0、1或2时，需要的翻转次数
        # 题目要求的就是dp(len(leaves) - 1)[2]
        # 由定义已知(0 < i < len(leaves))：
        # dp(i)[0] = dp[i-1][0] + int(leaves[i] == 'y')
        # dp(i)[1] = min(dp(i-1)[0], dp[i-1][1]) + int(leaves[i] == 'r)
        # dp(i)[2] = min(dp(i-1)[1], dp[i-1][2]) + int(leaves[i] == 'y') 
        dp = [int(leaves[0] == 'y'), float("inf"), float("inf")]
        l = len(leaves)
        for leave in leaves[1:]:
            dp[2] = min(dp[1], dp[2]) + int(leave == 'y')
            dp[1] = min(dp[0], dp[1]) + int(leave == 'r')
            dp[0] = dp[0] + int(leave == 'y')
        
        return dp[2]

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOperations("rrryyyrryyyrr"))
    print(solution.minimumOperations("ryr"))
