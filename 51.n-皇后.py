#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-31 19:54:48
LastEditors: Thomas Young
LastEditTime: 2020-08-31 23:14:54
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

# 示例:
# 输入: 4
# 输出: [
#     [".Q..",  // 解法 1
#      "...Q",
#      "Q...",
#      "..Q."],

#     ["..Q.",  // 解法 2
#      "Q...",
#      "...Q",
#      ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。

# 提示：
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
# 当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。
# （引用自 百度百科 - 皇后 ）
# 1 <= n <= 9

# Hard
from typing import List
# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        cols = [False for i in range(n)]
        diag = [False for i in range(n << 1)]
        backdiag = [False for i in range(n << 1)]
        res = []

        def placeQueen(row: int, col: int):
            cols[col] = True
            diag[row + col] = True
            backdiag[col - row + n] = True
            board[row][col] = 'Q'

        def replaceQueen(row: int, col: int):
            cols[col] = False
            diag[row + col] = False
            backdiag[col - row + n] = False
            board[row][col] = '.'

        def canPlaceQueen(row: int, col: int):
            return not (cols[col] or diag[row + col] or backdiag[col - row + n])

        def solve(row: int):
            if row == n:  # 求解成功
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if board[row][col] == '.' and canPlaceQueen(row, col):
                    placeQueen(row, col)
                    solve(row + 1)  # 放置下一行
                    replaceQueen(row, col)

        solve(0)

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
