#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

# 请返回 封闭岛屿 的数目。


# 示例 1：
# 输入：grid = [[1,1,1,1,1,1,1,0],
#              [1,0,0,0,0,1,1,0],
#              [1,0,1,0,1,1,1,0],
#              [1,0,0,0,0,1,0,1],
#              [1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

# 示例 2：
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1

# 示例 3：
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2


# 提示：
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

from collections import deque
from typing import List
# @lc code=start


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        DIR = [1, 0, -1, 0, 1]
        m, n = len(grid), len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    qu = deque([[i, j]])
                    valid = True

                    while qu:
                        x, y = qu.popleft()
                        grid[x][y] = -1
                        for k in range(4):
                            nx, ny = x+DIR[k], y+DIR[k+1]
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                valid = False
                            elif grid[nx][ny] == 0:
                                qu.append([nx, ny])

                    if valid:
                        res += 1

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
          1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))  # 2
    print(solution.closedIsland(
        [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))  # 1
    print(solution.closedIsland(
        [[1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1]]))  # 2
