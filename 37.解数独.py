#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-15 06:05:53
@LastEditors: Thomas Young
@LastEditTime: 2020-06-15 14:25:08
'''
#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。

# 示例 1：
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

# Note:
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# Hard
from typing import List
# @lc code=start


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def setNum(row: int, col: int, val: int):
            '''
            设置某格
            '''
            flag = 1 << (val - 1)
            rows[row] |= flag
            cols[col] |= flag
            boxes[boxIdx(row, col)] |= flag
            board[row][col] = str(val)

        def clearNum(row: int, col: int):
            '''
            撤销对某格的设置
            '''
            val = int(board[row][col])
            flag = (~(1 << (val - 1))) & MASK
            rows[row] &= flag
            cols[col] &= flag
            boxes[boxIdx(row, col)] &= flag
            board[row][col] = '.'

        def getAvailNum(row: int, col: int) -> List[int]:
            '''
            返回某格可能的数字，它必须是rows、cols、boxes里都没设置的位对应的数字
            '''
            flag = (~(rows[row] | cols[col] |
                      boxes[boxIdx(row, col)])) & MASK  # 位置为1的，都为可用的数字
            return [i for i in range(1, 10) if (1 << (i - 1) & flag)]

        def setNextNum(row: int, col: int):
            '''
            设置下一个格
            '''
            if row == N - 1 and col == N - 1:
                nonlocal solved
                solved = True
            else:
                if col == N - 1:
                    col = 0
                    row += 1
                else:
                    col += 1
                backTrace(row, col)

        def backTrace(row: int, col: int):
            '''
            回溯求解
            '''
            if board[row][col] == '.':
                availNums = getAvailNum(row, col)
                if availNums:
                    for num in availNums:
                        setNum(row, col, num)
                        setNextNum(row, col)  # 设置下一个格
                        if solved:  # 已经找到解了，后面的就不用遍历了
                            return
                        clearNum(row, col)
            # 设置下一个格
            else:
                setNextNum(row, col)

        n = 3  # 小块边长
        N = 9  # 行长
        MASK = (1 << N) - 1
        def boxIdx(row, col): return (row // 3) * 3 + (col // 3)  # 小方块序号

        # 分别记录每行、每列，每个小方格的已用数字情况
        rows = [0 for i in range(N)]
        cols = [0 for i in range(N)]
        boxes = [0 for i in range(N)]

        # 初始化
        for row, line in enumerate(board):
            for col, c in enumerate(line):
                if c != '.':
                    d = int(c)
                    setNum(row, col, d)

        # 回溯求解
        solved = False  # 是否已得解
        backTrace(0, 0)

        if solved:
            return board
        else:
            return None  # 无解

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveSudoku([
        list('53..7....'),
        list('6..195...'),
        list('.98....6.'),
        list('8...6...3'),
        list('4..8.3..1'),
        list('7...2...6'),
        list('.6....28.'),
        list('...419..5'),
        list('....8..79')
    ]), sep='\n')
