#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-16 22:09:25
@LastEditors: Thomas Young
@LastEditTime: 2020-06-16 23:27:05
'''
#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2


# 提示：
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是[−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)  # 商是否为负数

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        multiple, factor = divisor, 1
        while dividend > multiple:  # 先上推到最接近的倍数
            tmp = multiple << 1
            if tmp > dividend:
                break
            multiple = tmp
            factor <<= 1

        while dividend >= multiple or multiple > divisor:
            while dividend < multiple and multiple != divisor:
                multiple >>= 1
                factor >>= 1
            if dividend < divisor:
                break
            dividend -= multiple
            quotient += factor

        # return -quotient if neg else quotient
        # 不加下面的处理，测试用例过不去，其实python3的int范围理论上是无限的
        quotient = -quotient if neg else quotient
        if quotient > 2147483647:
            quotient = 2147483647
        elif quotient < -2147483648:
            quotient = -2147483648
        return quotient

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(7, -3))
    print(solution.divide(256, -13))
    print(solution.divide(-2147483648, -1))
