#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-30 08:36:27
LastEditors: Thomas Young
LastEditTime: 2020-10-30 08:48:07
'''
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿
# （或者说，一个或多个表示陆地的格子相连组成的岛屿）。

# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格
# 为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

# 示例:
# 输入:
# [[0, 1, 0, 0],
#  [1, 1, 1, 0],
#  [0, 1, 0, 0],
#  [1, 1, 0, 0]]
# 输出: 16

# 解释: 它的周长是下面图片中的 16 个黄色的边：

from typing import List
# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        sum = 0
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                if col:
                    if ri == 0 or grid[ri - 1][ci] == 0:
                        sum += 1
                    if ci == 0 or row[ci - 1] == 0:
                        sum += 1
                    if ci == len(row) - 1 or row[ci + 1] == 0:
                        sum += 1
                    if ri == len(grid) - 1 or grid[ri + 1][ci] == 0:
                        sum += 1
        return sum
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.islandPerimeter([[0, 1, 0, 0],
                                    [1, 1, 1, 0],
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0]]))
