#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-20 20:46:18
LastEditors: Thomas Young
LastEditTime: 2020-09-21 09:01:53
'''
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:
# 输入:
# [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
# 输出:
# [
#     [1, 0, 1],
#     [0, 0, 0],
#     [1, 0, 1]
# ]

# 示例 2:
# 输入:
# [
#     [0, 1, 2, 0],
#     [3, 4, 5, 2],
#     [1, 3, 1, 5]
# ]
# 输出:
# [
#     [0, 0, 0, 0],
#     [0, 4, 5, 0],
#     [0, 3, 1, 0]
# ]

# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？

from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix and matrix[0]:
            N, M = len(matrix), len(matrix[0])
            # 需要O(1)的额外空间——firstZero
            firstZero = 0 in matrix[0] # 记录首行是否要置零

            for row in range(1, N):
                for col in range(M):
                    if matrix[row][col] == 0: # 说明第row行和第col列要置0
                        matrix[0][col] = 0
                        matrix[row][0] = 0
            
            for row in range(1, N):
                for col in range(1, M):
                    if matrix[row][0] == 0 or matrix[0][col] == 0:
                        matrix[row][col] = 0
            
            if matrix[0][0] == 0: # first column
                for row in range(1, N):
                    matrix[row][0] = 0

            if firstZero: # 最后干
                for col in range(M):
                    matrix[0][col] = 0


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    solution.setZeroes(matrix)
    print(matrix)

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    solution.setZeroes(matrix)
    print(matrix)
