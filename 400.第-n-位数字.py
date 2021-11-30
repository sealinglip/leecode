#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-11-30 21:02:54
LastEditors: Thomas Young
LastEditTime: 2021-11-30 21:21:43
'''
#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# 给你一个整数 n ，请你在无限的整数序列[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。

# 示例 1：
# 输入：n = 3
# 输出：3

# 示例 2：
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。

# 提示：
# 1 <= n <= 2^31 - 1
# 第 n 位上的数字是按计数单位（digit）从前往后数的第 n 个数，参见 示例 2 。

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1 ~ 9: 共 9 位 (9 * 1)
        # 10 ~ 99: 共 180 位（90 * 2）
        # 100 ~ 999: 共 2700 位 (900 * 3)
        # 依此类推，n位数合起来的位数为 9 * 10^(n-1) * n

        i = 1
        while n > 0:
            c = 9 * (10 ** (i - 1)) * i
            if n > c:
                # 还在后面的区间
                n -= c
                i += 1
            else:
                # 落在本区间
                # 算出落在哪个数上
                num = (n - 1) // i + 10 ** (i - 1)
                remainder = n % i
                return int(str(num)[remainder-1])
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findNthDigit(3)) # 3
    print(solution.findNthDigit(11)) # 0