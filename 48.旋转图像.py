#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-31 16:41:33
LastEditors: Thomas Young
LastEditTime: 2020-08-31 19:53:40
'''
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。

# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 示例 1:
# 给定 matrix =
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ],
# 原地旋转输入矩阵，使其变为:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

# 示例 2:
# 给定 matrix =
# [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ],
# 原地旋转输入矩阵，使其变为:
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]

from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        N = len(matrix)
        if N < 2:
            return
        
        odd = N & 1 # 维度是否为奇数
        n = N >> 1 # 需处理n行
        m = N - n # 需处理m列
        
        for row in range(n):
            for col in range(m):
                # 先保存初始值
                tmp = matrix[row][col]
                matrix[row][col] = matrix[N - col - 1][row]
                matrix[N - col - 1][row] = matrix[N - row - 1][N - col - 1]
                matrix[N - row - 1][N - col - 1] = matrix[col][N - row - 1]
                matrix[col][N - row - 1] = tmp

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(matrix)
    print(matrix)

    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solution.rotate(matrix)
    print(matrix)


