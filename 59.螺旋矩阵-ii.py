#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-06 09:26:15
LastEditors: Thomas Young
LastEditTime: 2020-09-06 09:32:11
'''
#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

# 示例:
# 输入: 3
# 输出:
# [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]

from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
            
        res = [[0] * n for i in range(n)]
        lb, rb, ub, bb = 0, n - 1, 0, n - 1  # 左右上下的边界（闭区间）
        dir = 1  # 指针移动方向：1 右， 2 下， -1 左， -2 上
        num = 0
        while True:
            if dir == 1:  # 向右
                for i in range(lb, rb + 1):
                    num += 1
                    res[ub][i] = num
                if ub == bb:
                    break
                else:
                    ub += 1
                    dir = 2
            elif dir == 2:
                for i in range(ub, bb + 1):
                    num += 1
                    res[i][rb] = num
                if lb == rb:
                    break
                else:
                    rb -= 1
                    dir = -1
            elif dir == -1:
                for i in range(rb, lb - 1, -1):
                    num += 1
                    res[bb][i] = num
                if ub == bb:
                    break
                else:
                    bb -= 1
                    dir = -2
            else:
                for i in range(bb, ub - 1, -1):
                    num += 1
                    res[i][lb] = num
                if lb == rb:
                    break
                else:
                    lb += 1
                    dir = 1
        return res
        pass
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))
