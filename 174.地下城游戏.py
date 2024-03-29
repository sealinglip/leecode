#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
# 我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
# 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。


# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
# -2 (K) - 3	3
# -5 - 10	1
# 10	30 - 5 (P)


# 说明:
# 骑士的健康点数没有上限。
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

# Hard

from math import inf
from typing import List
# @lc code=start


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [inf] * (n + 1)  # 记dp[i] 为第i个房间能到终点的最小健康点数
        # 如果dp设计为从起点到第i个房间所需的最小健康点数，不满足状态转移方程的无后效性
        dp[-2] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minn = min(dp[j], dp[j+1])
                dp[j] = max(1, minn - dungeon[i][j])

        return dp[0]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]))
