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

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0) # 商是否为负数

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        multiple, factor = divisor, 1
        while dividend > multiple: # 先上推到最接近的倍数
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
