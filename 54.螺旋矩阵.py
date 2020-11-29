#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-02 09:12:45
LastEditors: Thomas Young
LastEditTime: 2020-09-02 09:29:18
'''
#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:
# 输入:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 输出: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# 示例 2:

# 输入:
# [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# 输出: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

from typing import List
# @lc code=start

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        lb, rb, ub, bb = 0, len(matrix[0]) - 1, 0, len(matrix) - 1 # 左右上下的边界（闭区间）
        dir = 1 # 指针移动方向：1 右， 2 下， -1 左， -2 上
        res = []
        while True:
            if dir == 1: # 向右
                for i in range(lb, rb + 1):
                    res.append(matrix[ub][i])
                if ub == bb:
                    break
                else:
                    ub += 1
                    dir = 2
            elif dir == 2:
                for i in range(ub, bb + 1):
                    res.append(matrix[i][rb])
                if lb == rb:
                    break
                else:
                    rb -= 1
                    dir = -1
            elif dir == -1:
                for i in range(rb, lb - 1, -1):
                    res.append(matrix[bb][i])
                if ub == bb:
                    break
                else:
                    bb -= 1
                    dir = -2
            else:
                for i in range(bb, ub - 1, -1):
                    res.append(matrix[i][lb])
                if lb == rb:
                    break
                else:
                    lb += 1
                    dir = 1
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(solution.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]))
