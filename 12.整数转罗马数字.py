#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 14:40:27
@LastEditors: Thomas Young
@LastEditTime: 2020-06-12 15:01:34
'''
#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        cs = []
        
        # 处理千位
        th = num // 1000
        cs.append(th * 'M')
        
        # 处理百位
        num -= th * 1000
        hun = num // 100
        cs.append(self.convertDigit(hun, "C", "D", "M"))

        # 处理十位
        num -= hun * 100
        dec = num // 10
        cs.append(self.convertDigit(dec, "X", "L", "C"))

        # 处理个位
        num -= dec * 10
        cs.append(self.convertDigit(num, "I", "V", "X"))

        return "".join(cs)

    def convertDigit(self, num: int, one: str, five: str, ten: str) -> str:
        if num == 9:
            return one + ten
        elif num == 4:
            return one + five
        elif num >= 5:
            return five + (num - 5) * one
        else:
            return num * one

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(27))
    print(solution.intToRoman(3))
    print(solution.intToRoman(4))
    print(solution.intToRoman(9))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))
