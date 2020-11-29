#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-13 08:34:05
@LastEditors: Thomas Young
@LastEditTime: 2020-06-13 08:59:01
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 爬n级台阶的方法就是爬n-1级和爬n-2级方法之和
        # 所以实际是个斐波那契数列问题
        # 初始值
        if n <= 2:
            return n
        else:
            pre = 1
            cur = 2
            for i in range(2, n):
                tmp = cur
                cur = tmp + pre
                pre = tmp
            return cur
        
# @lc code=end

