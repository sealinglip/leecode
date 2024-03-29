#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
from typing import List

# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 - 1 。

# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。


# 示例 1：
# 输入：grid = [[0, 1], [1, 0]]
# 输出：2

# 示例 2：
# 输入：grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
# 输出：4

# 示例 3：
# 输入：grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
# 输出：- 1


# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        DIR = [0, 1, 1, 0, -1, 1, -1, -1, 0]
        n = len(grid)

        # 广度优先搜索
        cells = [(0, 0)]
        res = 1
        visited = set(cells)
        while cells:
            nc = []
            for cell in cells:
                x, y = cell
                if x == n-1 and y == n-1:
                    return res

                for i in range(8):
                    nx, ny = x + DIR[i], y + DIR[i+1]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        cell = (nx, ny)
                        if cell not in visited:
                            nc.append(cell)
                            visited.add(cell)
            res += 1
            cells = nc

        return -1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestPathBinaryMatrix([[0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0], [
          0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0]]))  # 14
    print(solution.shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # 2
    print(solution.shortestPathBinaryMatrix(
        [[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
    print(solution.shortestPathBinaryMatrix(
        [[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1
    print(solution.shortestPathBinaryMatrix(
        [[0, 0, 0], [1, 1, 1], [1, 1, 0]]))  # -1
