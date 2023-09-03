#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。

# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。


# 示例 1：
# 输入：grid = [[1, 0], [0, 1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。

# 示例 2：
# 输入：grid = [[1, 0], [1, 1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。

# 示例 3：
# 输入：grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。


# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1

# 复习

from typing import List
# @lc code=start


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        colSet = {}
        rowSums = []
        res = 0
        for i, row in enumerate(grid):
            rowSum = 0
            counted = 0  # 记住因同一列有服务器而计数的服务器
            for j, x in enumerate(row):
                if x == 1:
                    rowSum += 1
                    if j in colSet:
                        # 本列出现过值
                        res += 1
                        counted += 1
                        # 判断本列之前出现的值有没有计入
                        if rowSums[colSet[j]] == 1:
                            # 没有计入的话补记
                            res += 1
                            rowSums[colSet[j]] = -1  # 清掉标记
                    else:
                        colSet[j] = i
            rowSums.append(rowSum)
            if rowSum > 1:
                res += rowSum - counted
        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countServers([[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0], [
          0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0]]))  # 9
    print(solution.countServers([[1, 0], [0, 1]]))  # 0
    print(solution.countServers([[1, 0], [1, 1]]))  # 3
    print(solution.countServers(
        [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))  # 4
