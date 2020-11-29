#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-02 16:27:30
@LastEditors: Thomas Young
@LastEditTime: 2020-07-03 14:17:32
'''
#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
# 在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。
# 进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）

# 示例 1:
# 输入: [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 示例 2:
# 输入: [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 示例 3:
# 输入: [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
# 说明:

# 1 <= grid.length = grid[0].length <= 50
# 0 <= grid[i][j] <= 1

# @lc code=start
from typing import List, Tuple
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid) # 地图边长
        dx = [0, 0, -1, 1] # 上下左右
        dy = [-1, 1, 0, 0] # 上下左右

        def getNeighbor(x: int, y: int) -> List[Tuple[int]]:
            '''
            获取[x,y]的邻居格
            '''
            neighbor = []
            for i in range(4):  # 上下左右来一遍
                x1, y1 = x + dx[i], y + dy[i]
                if 0 <= x1 < N and 0 <= y1 < N:
                    neighbor.append((x1, y1))

            return neighbor

        def getConnectedDomain(x: int, y: int, index: int) -> int:
            '''
            给定x，y，计算x，y所在连通域的面积
            '''
            grid[x][y] = index
            area = 1
            for x1, y1 in getNeighbor(x, y): # 上下左右来一遍
                if grid[x1][y1] == 1:
                    area += getConnectedDomain(x1, y1, index)
            return area

        area = [0, 0]  # 记录连通域的面积（第一个元素没有用，只是为了跟index保持一致）
        index = 2 # 从2开始，避免把第一个连通域的格子都赋值成0，也避免和本来的1混淆
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area.append(getConnectedDomain(x, y, index))
                    index += 1

        maxArea = max(area)
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    a = 1
                    indexSet = set()
                    for x1, y1 in getNeighbor(x, y):
                        if grid[x1][y1] != 0:
                            indexSet.add(grid[x1][y1])
                    if indexSet:
                        for idx in indexSet:
                            a += area[idx]
                    maxArea = max(a, maxArea)
        return maxArea
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestIsland([[1, 0], [0, 1]]))
    print(solution.largestIsland([[0, 1], [1, 0]]))
    print(solution.largestIsland([[1, 1], [0, 1]]))
    print(solution.largestIsland([[1, 0], [1, 1]]))
    print(solution.largestIsland([[1, 1], [1, 1]]))
