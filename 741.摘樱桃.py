#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#
# 一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：

# 0 表示这个格子是空的，所以你可以穿过它。
# 1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
# -1 表示这个格子里有荆棘，挡着你的路。
# 你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：

# 从位置(0, 0) 出发，最后到达(N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
# 当到达(N-1, N-1) 后，你要继续走，直到返回到(0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
# 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
# 如果在(0, 0) 和(N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。

# 示例 1:
# 输入: grid =
# [[0, 1, -1],
#  [1, 0, -1],
#  [1, 1,  1]]
# 输出: 5
# 解释：
# 玩家从（0, 0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
# 在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0, 1, -1], [0, 0, -1], [0, 0, 0]]。
# 接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
# 在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。

# 说明:
# grid 是一个 N * N 的二维数组，N的取值范围是1 <= N <= 50。
# 每一个 grid[i][j] 都是集合 {-1, 0, 1}其中的一个数。
# 可以保证起点 grid[0][0] 和终点 grid[N-1][N-1] 的值都不会是 - 1。

# Hard
# 复习

from math import inf
from typing import List
# @lc code=start


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 动规
        # 折返可以转换为两人一起走，能采摘到的最大🍒数
        # 记dp(k, x1, x2) 为 两人从 (0, 0) 同时出发，分别到达(x1, k-x1)，(x2, k-x2) 时摘到的最大🍒数，x1 <= x2
        # 有dp(k, x1, x2) = -∞ if grid[x1][k-x1] == -1 or grid[x2][k-x2] == -1 # 有荆棘表示场景不合法
        # dp(0, 0, 0) = grid[0][0]
        # dp(k, x1, x2) = max(dp(k-1, x1, x2), dp(k-1, x1-1, x2-1), dp(k-1, x1, x2-1), dp(k-1, x1-1, x2)) + grid[x1][k-x1] + grid[x2][k-x2]?
        #         # 如果 x1 == x2，说明此时两人位置重合，则只加grid[x1][k-x1]

        N = len(grid)
        dp = [[[-inf] * N for _ in range(N)] for _ in range(2 * N - 1)]
        dp[0][0][0] = grid[0][0]

        for k in range(1, 2 * N - 1):
            # 注意x1的遍历范围和k的关系，0 <= x1 < N，0 <= k-x1 < N (即当前横纵坐标都应该在[0, N)范围里)
            for x1 in range(max(0, k - N + 1), min(k + 1, N)):
                y1 = k - x1
                if grid[x1][y1] == -1:  # 路不通
                    continue
                for x2 in range(x1, min(k + 1, N)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:  # 路不通
                        continue

                    res = dp[k-1][x1][x2]  # 从上一步到这，大家都是向右
                    if x1:
                        res = max(res, dp[k-1][x1-1][x2])  # A 向下，B向右
                    if x2:
                        res = max(res, dp[k-1][x1][x2-1])  # A 向右，B向下
                        if x1:
                            res = max(res, dp[k-1][x1-1][x2-1])  # 大家都向下
                    res += grid[x1][y1]
                    if x1 != x2:
                        res += grid[x2][y2]

                    dp[k][x1][x2] = res

        return max(dp[2 * N - 2][N - 1][N - 1], 0)
        # @lc code=end


if __name__ == "__main__":
    grid = [[0, 1, -1],
            [1, 0, -1],
            [1, 1,  1]]
    solution = Solution()
    print(solution.cherryPickup(grid))  # 5
    print(solution.cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]])) # 0
