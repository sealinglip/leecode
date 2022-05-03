#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-09-11 21:25:12
LastEditors: Thomas Young
LastEditTime: 2021-09-11 22:58:39
'''
#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

# 示例 1:
# 输入: 5
# 输出: 5
# 解释:
# 下面是带有相应二进制表示的非负整数 <= 5：
# 0: 0
# 1: 1
# 2: 10
# 3: 11
# 4: 100
# 5: 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
# 说明: 1 <= n <= 10^9

# Hard

# @lc code=start


class Solution:
    def findIntegers(self, n: int) -> int:
        # 先判断n是2的几次方到几次方之间
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        res = 0
        pre = 0
        # n从高位开始判断
        for i in range(29, -1, -1):
            if n & (1 << i):
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1  # 记录本位
            else:
                pre = 0

            if i == 0:
                res += 1
        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findIntegers(5))  # 5
    print(solution.findIntegers(7))  # 5
