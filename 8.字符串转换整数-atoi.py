#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 06:53:00
@LastEditors: Thomas Young
@LastEditTime: 2020-06-12 07:46:03
'''
#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        str, neg = str.strip(), False
        if not str:
            return 0

        if str[0] == '+' or str[0] == '-': #处理可能的符号
            neg = str[0] == '-'
            str = str[1:]
            
        if not str or not str[0].isdigit(): #如果开头不是数字，直接返回0
            return 0

        digitLen = 0
        for c in str:
            if c.isdigit():
                digitLen += 1
            else:
                break

        res = int(str[:digitLen])
        if neg:
            res = -res
        
        # 判断范围
        if res > (1 << 31) - 1:
            res = (1 << 31) - 1
        elif res < -(1 << 31):
            res = -(1 << 31)
        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("    -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))
