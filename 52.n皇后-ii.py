#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-01 08:57:49
LastEditors: Thomas Young
LastEditTime: 2020-09-01 09:01:23
'''
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。

# 示例:
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#     [".Q..",  // 解法 1
#      "...Q",
#      "Q...",
#      "..Q."],

#     ["..Q.",  // 解法 2
#         "Q...",
#         "...Q",
#         ".Q.."]
# ]


# 提示：
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
# 当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N-1 步，可进可退。
# 1 <= n <= 9

# Hard
# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [False for i in range(n)]
        cols = [False for i in range(n)]
        diag = [False for i in range(n << 1)]
        backdiag = [False for i in range(n << 1)]
        res = 0

        def placeQueen(row: int, col: int):
            rows[row] = True
            cols[col] = True
            diag[row + col] = True
            backdiag[col - row + n] = True

        def replaceQueen(row: int, col: int):
            rows[row] = False
            cols[col] = False
            diag[row + col] = False
            backdiag[col - row + n] = False

        def canPlaceQueen(row: int, col: int):
            return not (rows[row] or cols[col] or diag[row + col] or backdiag[col - row + n])

        def solve(row: int):
            if row == n:  # 求解成功
                nonlocal res
                res += 1
                return

            for col in range(n):
                if canPlaceQueen(row, col):
                    placeQueen(row, col)
                    solve(row + 1)  # 放置下一行
                    replaceQueen(row, col)

        solve(0)

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.totalNQueens(4))
