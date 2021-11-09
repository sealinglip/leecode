#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。


# 示例 1:
# 输入: heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1 = 4。

# 示例 2:
# 输入: heightMap = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [
#     3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
# 输出: 10


# 提示:
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4

from typing import List
# @lc code=start
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        # 记录节点访问状态
        visited = [[False] * n for _ in range(m)]
        # 优先队列
        queue = []
        # 将边界点先进队列
        for i in range(m):
            heapq.heappush(queue, (heightMap[i][0], i, 0))
            heapq.heappush(queue, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True

        for j in range(1, n - 1):
            heapq.heappush(queue, (heightMap[0][j], 0, j))
            heapq.heappush(queue, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True

        # 遍历方向
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        res = 0
        while queue:
            h, x, y = heapq.heappop(queue)
            for deltax, deltay in dir:
                nx, ny = x + deltax, y + deltay
                # 在矩阵范围内才处理
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # 这个代表”我“跟你挨着，”我“是你周边最短的板（因为”我“从队列里先出来），”我“的高度决定了你能装多少水
                    if h > heightMap[nx][ny]:
                        res += h - heightMap[nx][ny]
                    heapq.heappush(queue, (max(h, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True  # 标记已遍历

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.trapRainWater(
        [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))  # 4
    print(solution.trapRainWater(
        [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))  # 10
