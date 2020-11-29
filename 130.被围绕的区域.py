#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-08 17:22:00
LastEditors: Thomas Young
LastEditTime: 2020-11-08 17:44:02
'''
#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

# 示例:
# X X X X
# X O O X
# X X O X
# X O X X

# 运行你的函数后，矩阵变为：
# X X X X
# X X X X
# X X X X
# X O X X

# 解释:
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与
# 边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

from typing import List
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        M, N = len(board), len(board[0])
        mark = set() # 记录标记跟边界相连的'O'

        def markPoint(row: int, col: int, dir: int):
            """[summary]

            Args:
                row (int): 行坐标
                col (int): 列坐标
                dir (int): 方向：1：来路为上；2：来路为右；3：来路为下；4：来路为左
            """
            key = (row, col)
            if key in mark:
                return
            else:
                mark.add(key)
                if dir != 1 and row > 0 and board[row - 1][col] == 'O':
                    markPoint(row - 1, col, 3)
                if dir != 2 and col < N - 1 and board[row][col + 1] == 'O':
                    markPoint(row, col + 1, 4)
                if dir != 3 and row < M - 1 and board[row + 1][col] == 'O':
                    markPoint(row + 1, col, 1)
                if dir != 4 and col > 0 and board[row][col - 1] == 'O':
                    markPoint(row, col - 1, 2)

        for i in range(M):
            if board[i][0] == 'O':
                markPoint(i, 0, 4)
            if board[i][N - 1] == 'O':
                markPoint(i, N - 1, 2)
        for j in range(N):
            if board[0][j] == 'O':
                markPoint(0, j, 1)
            if board[M - 1][j] == 'O':
                markPoint(M - 1, j, 3)

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if board[i][j] == 'O' and ((i, j) not in mark):
                    board[i][j] = 'X'

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    solution.solve(matrix)
    print(matrix)