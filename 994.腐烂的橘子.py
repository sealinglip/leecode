#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。


# 示例 1：
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4

# 示例 2：
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。

# 示例 3：
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] 仅为 0、1 或 2

from typing import List
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 找出所有的1
        fresh = set()
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    fresh.add((i, j))

        def rotable(i: int, j: int) -> bool:
            # 判断旁边有没有烂橘子
            return (i > 0 and grid[i-1][j] == 2) or (i < m-1 and grid[i+1][j] == 2) or (j > 0 and grid[i][j-1] == 2) or (j < n-1 and grid[i][j+1] == 2)

        res = 0
        while fresh:
            left = len(fresh)
            # 挨个看好柿子这轮是不是要完蛋
            rot = set()
            for i, j in fresh:
                if rotable(i, j):
                    rot.add((i, j))
            fresh = fresh.difference(rot)
            for i, j in rot:
                grid[i][j] = 2

            if len(fresh) == left:
                return -1
            res += 1
            
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(solution.orangesRotting([[0,2]])) # 0