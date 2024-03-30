#
# @lc app=leetcode.cn id=2617 lang=python3
#
# [2617] 网格图中最少访问的格子数
#
# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。

# 当你在格子 (i, j) 的时候，你可以移动到以下格子之一：

# 满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
# 满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
# 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。


# 示例 1：
# 输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# 输出：4
# 解释：上图展示了到达右下角格子经过的 4 个格子。

# 示例 2：
# 输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# 输出：3
# 解释：上图展示了到达右下角格子经过的 3 个格子。

# 示例 3：
# 输入：grid = [[2,1,0],[1,0,0]]
# 输出：-1
# 解释：无法到达右下角格子。
 
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 0 <= grid[i][j] < m * n
# grid[m - 1][n - 1] == 0

# Hard
# 复习

from collections import deque
import heapq
from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1
        
        # # 下面的解法会内存溢出，改为入栈的时候就标记为已访问
        # # 内存不溢出了，TLE
        # # 广度优先遍历
        # q = deque([(0, 0, 1)])
        # while q:
        #     x, y, step = q.popleft()
        #     v = abs(grid[x][y])
        #     if v > 0:
        #         # 入栈从此处可触达之格子
        #         for i in range(y+1, min(y+v+1, n)):
        #             if (x == m-1 and i == n-1):
        #                 return step + 1
        #             if grid[x][i] > 0:
        #                 q.append((x, i, step+1))
        #                 grid[x][i] = -grid[x][i] # 标记为已访问过
        #         for i in range(x+1, min(x+v+1, m)):
        #             if (i == m-1 and y == n-1):
        #                 return step + 1
        #             if grid[i][y] > 0:
        #                 q.append((i, y, step+1))
        #                 grid[i][y] = -grid[i][y] # 标记为已访问过

        # 换解法
        # 从左到右，从上到下，计算step
        # 每一列单独维护小顶堆
        # 行只用维护一个小顶堆
        rowQu = [(1, 0)] # 里面的元素为(step, j)，step为到某格的步数，j为某格的纵坐标
        colQu = [[] for _ in range(n)] # colQu[j] 里的元素为(step, i)，step为到某格的步数，i为某格的横坐标
        colQu[0].append((1, 0))
        res = -1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                while rowQu and rowQu[0][1] + grid[i][rowQu[0][1]] < j: # 够不着当前格了，肯定也够不着后续的格，从优先队列里出来
                    heapq.heappop(rowQu)

                s = inf
                if rowQu:
                    s = min(s, rowQu[0][0] + 1)
                
                while colQu[j] and colQu[j][0][1] + grid[colQu[j][0][1]][j] < i:
                    heapq.heappop(colQu[j])
                if colQu[j]:
                    s = min(s, colQu[j][0][0] + 1)

                if i == m - 1 and j == n - 1:
                    res = -1 if s == inf else s
                    break
                if s != inf:
                    heapq.heappush(rowQu, (s, j))
                    heapq.heappush(colQu[j], (s, i))
            rowQu.clear() # 清理行堆

        return res
                    

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumVisitedCells([[7,12,11,11,4],[10,5,16,15,7],[7,9,6,16,7],[1,13,3,16,0]])) # 3
    print(solution.minimumVisitedCells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]])) # 3
    print(solution.minimumVisitedCells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]])) # 4
    print(solution.minimumVisitedCells([[2,1,0],[1,0,0]])) # -1
