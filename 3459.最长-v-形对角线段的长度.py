#
# @lc app=leetcode.cn id=3459 lang=python3
#
# [3459] 最长 V 形对角线段的长度
#
# https://leetcode.cn/problems/length-of-longest-v-shaped-diagonal-segment/description/
#
# algorithms
# Hard (51.60%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 5.6K
# Testcase Example:  '[[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]'
#
# 给你一个大小为 n x m 的二维整数矩阵 grid，其中每个元素的值为 0、1 或 2。
# 
# V 形对角线段 定义如下：
# 线段从 1 开始。
# 后续元素按照以下无限序列的模式排列：2, 0, 2, 0, ...。
# 该线段：
# 起始于某个对角方向（左上到右下、右下到左上、右上到左下或左下到右上）。
# 沿着相同的对角方向继续，保持 序列模式 。
# 在保持 序列模式 的前提下，最多允许 一次顺时针 90 度转向 另一个对角方向。
# 
# 返回最长的 V 形对角线段 的 长度 。如果不存在有效的线段，则返回 0。
# 
# 
# 示例 1：
# 输入： grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# 输出： 5
# 解释：
# 最长的 V 形对角线段长度为 5，路径如下：(0,2) → (1,3) → (2,4)，在 (2,4) 处进行 顺时针 90 度转向 ，继续路径为
# (3,3) → (4,2)。
# 
# 示例 2：
# 输入： grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# 输出： 4
# 解释：
# 最长的 V 形对角线段长度为 4，路径如下：(2,3) → (3,2)，在 (3,2) 处进行 顺时针 90 度转向 ，继续路径为 (2,1) →
# (1,0)。
# 
# 示例 3：
# 输入： grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
# 输出： 5
# 解释：
# 最长的 V 形对角线段长度为 5，路径如下：(0,0) → (1,1) → (2,2) → (3,3) → (4,4)。
# 
# 示例 4：
# 输入： grid = [[1]]
# 输出： 1
# 解释：
# 最长的 V 形对角线段长度为 1，路径如下：(0,0)。
# 
# 
# 提示：
# n == grid.length
# m == grid[i].length
# 1 <= n, m <= 500
# grid[i][j] 的值为 0、1 或 2。
# 
# 
#

from functools import cache
from typing import List
# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIR = [(1,1), (-1,1), (-1,-1), (1,-1)]
        n, m = len(grid), len(grid[0])

        @cache
        def search(x: int, y: int, dir: int, turn: bool, expect: int) -> int:
            '''
            从(x,y)出发，方向为dir，由turn标志是否还能转向，expect为(x,y)期望的值，能构建的对角线的最长长度
            '''
            # 如果坐标超限，或者值不合预期，直接返回0
            if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] != expect:
                return 0
            
            res = 1 + search(x+DIR[dir][0], y+DIR[dir][1], dir, turn, 2-expect)
            if turn:
                dir = (dir + 1) % 4
                res = max(res, 1 + search(x+DIR[dir][0], y+DIR[dir][1], dir, False, 2-expect))
            
            return res
            
        res = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    for dir in range(4):
                        res = max(res, 1 + search(x+DIR[dir][0], y+DIR[dir][1], dir, True, 2))
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])) # 5
    print(solution.lenOfVDiagonal([[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])) # 4
    print(solution.lenOfVDiagonal([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]])) # 5
    print(solution.lenOfVDiagonal([[1]])) # 1
