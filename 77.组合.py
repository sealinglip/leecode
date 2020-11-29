#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-08 08:36:35
LastEditors: Thomas Young
LastEditTime: 2020-09-08 08:49:41
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#     [2, 4],
#     [3, 4],
#     [2, 3],
#     [1, 2],
#     [1, 3],
#     [1, 4],
# ]

from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n:
            return []
        
        res = []
        flag = [True] * (n + 1) # available
        stack = [None] * k
        def setNthNum(nth: int, begin: int):
            for i in range(begin, n + 1):
                if flag[i]:
                    flag[i] = False
                    stack[nth] = i
                    if nth == k - 1:
                        res.append(stack[:])
                    else:
                        setNthNum(nth + 1, i + 1)
                    flag[i] = True
        setNthNum(0, 1)

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4, 2))
