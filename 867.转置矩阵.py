#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-02-25 21:05:05
LastEditors: Thomas Young
LastEditTime: 2021-02-25 21:11:45
'''
#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]

# 示例 2：
# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
 

# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9


from typing import List
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        return [[matrix[i][j] for i in range(M)] for j in range(N)]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.transpose([[1, 2, 3], [4, 5, 6]]))
