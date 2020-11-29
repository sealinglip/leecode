#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-02 08:43:51
LastEditors: Thomas Young
LastEditTime: 2020-09-02 09:11:56
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:
# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # 牛顿迭代
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(8))
    print(solution.mySqrt(4))
    print(solution.mySqrt(6))
    print(solution.mySqrt(9))
