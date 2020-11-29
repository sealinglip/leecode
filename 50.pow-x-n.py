#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-06 08:20:25
@LastEditors: Thomas Young
@LastEditTime: 2020-07-06 08:36:59
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

# 示例 1:
# 输入: 2.00000, 10
# 输出: 1024.00000

# 示例 2:
# 输入: 2.10000, 3
# 输出: 9.26100

# 示例 3:
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25

# 说明:
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是[−2^31, 2^31 − 1] 。

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        else:
            result = 1
            exp, power = 1, x
            while exp <= n:
                if exp & n:
                    result *= power
                exp <<= 1
                if exp > n:
                    break
                power *= power 
            return result
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2, -2))
