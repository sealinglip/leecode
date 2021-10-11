#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-10-10 21:42:35
LastEditors: Thomas Young
LastEditTime: 2021-10-10 21:59:11
'''
#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。


# 示例 1：
# 输入：n = 5
# 输出：2
# 解释：因为第三行不完整，所以返回 2 。

# 示例 2：
# 输入：n = 8
# 输出：3
# 解释：因为第四行不完整，所以返回 3 。


# 提示：
# 1 <= n <= 2^31 - 1

# @lc code=start
from math import floor, sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 满k行阶梯的硬币数范围是
        # k * (k + 1) / 2 <= n < (k + 2) * (k + 1) / 2
        # => (2k + 1) ^ 2 <= 8n + 1 < (2k + 3) ^ 2
        # 已知n，求k
        return (floor(sqrt(n * 8 + 1)) - 1) >> 1
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.arrangeCoins(6)) # 3
    print(solution.arrangeCoins(5)) # 2
    print(solution.arrangeCoins(8)) # 3
