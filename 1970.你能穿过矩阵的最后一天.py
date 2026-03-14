#
# @lc app=leetcode.cn id=1970 lang=python3
#
# [1970] 你能穿过矩阵的最后一天
#
# https://leetcode.cn/problems/last-day-where-you-can-still-cross/description/
#
# algorithms
# Hard (52.47%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 9.9K
# Testcase Example:  '2\n2\n[[1,1],[2,1],[1,2],[2,2]]'
#
# 给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。
# 一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，其中
# cells[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。
# 
# 你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意
# 格子。你只能沿着 四个 基本方向移动（也就是上下左右）。
# 
# 请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。
# 
# 
# 示例 1：
# 输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# 输出：2
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 2 天。
# 
# 示例 2：
# 输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# 输出：1
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 1 天。
# 
# 示例 3：
# 输入：row = 3, col = 3, cells =
# [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# 输出：3
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 3 天。
# 
# 
# 提示：
# 2 <= row, col <= 2 * 10^4
# 4 <= row * col <= 2 * 10^4
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# cells 中的所有格子坐标都是 唯一 的。
# 
# 
#

from typing import List
# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.group = list(range(n))

    def find(self, x: int) -> int:
        if x != self.group[x]:
            self.group[x] = self.find(self.group[x])
        return self.group[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.group[x] = y

    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # 并查集 + 倒推

        n = row * col
        uf = UnionFind(n + 2) # n和n+1分别代表首行和末行，其他代表单元格

        land = [False] * n # 记录单元格是不是陆地
        res = 0
        for i in range(n-1, -1, -1):
            x, y = cells[i]
            # 修正为0-based
            x = x - 1
            y = y - 1
            idx = x * col + y
            land[idx] = True
            # 更新连通集
            if x == 0:
                uf.union(n, idx)
            elif x > 0 and land[idx - col]:
                uf.union(idx, idx - col)
            if x == row - 1:
                uf.union(n+1, idx)
            elif x < row - 1 and land[idx + col]:
                uf.union(idx, idx + col)
            if y > 0 and land[idx - 1]:
                uf.union(idx, idx - 1)
            if y < col - 1 and land[idx + 1]:
                uf.union(idx, idx + 1)
            if uf.isConnected(n, n + 1):
                res = i
                break
            
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]])) # 2
    print(solution.latestDayToCross(2, 2, [[1,1],[1,2],[2,1],[2,2]])) # 1
    print(solution.latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]])) # 3