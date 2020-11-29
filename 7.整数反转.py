#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-11 23:28:33
@LastEditors: Thomas Young
@LastEditTime: 2020-06-11 23:54:00
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if not x: # 如果为0
            return x

        s = str(x)
        neg = s[0] == '-'

        stop = len(s)
        while s[stop - 1] == '0':
            stop -= 1
        
        s = s[stop - 1: 0: -1] if neg else s[stop - 1: : -1]
        v = int(s)
        if neg:
            v = -v
        if v >= (1 << 31) or v < -(1 << 31):
            v = 0
        return v


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(-123))
    print(solution.reverse(-2147483648))
