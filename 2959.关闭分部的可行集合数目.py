#
# @lc app=leetcode.cn id=2959 lang=python3
#
# [2959] 关闭分部的可行集合数目
#
# 一个公司在全国有 n 个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。
# 公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（也可能不关闭任何分部），同时保证剩下的分部之间两两互相可以到达且最远距离不超过 maxDistance 。
# 两个分部之间的 距离 是通过道路长度之和的 最小值 。
# 给你整数 n ，maxDistance 和下标从 0 开始的二维整数数组 roads ，其中 roads[i] = [ui, vi, wi] 表示一条从 ui 到 vi 长度为 wi的 无向 道路。
# 请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过 maxDistance。
# 注意，关闭一个分部后，与之相连的所有道路不可通行。
# 注意，两个分部之间可能会有多条道路。

# 示例 1：
# 输入：n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
# 输出：5
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [2] ，剩余分部为 [0,1] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 5 种可行的关闭方案。

# 示例 2：
# 输入：n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
# 输出：7
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0,1,2] ，它们之间的最远距离为 4 。
# - 关闭分部集合 [0] ，剩余分部为 [1,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [1] ，剩余分部为 [0,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 7 种可行的关闭方案。

# 示例 3：
# 输入：n = 1, maxDistance = 10, roads = []
# 输出：2
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0] 。
# - 关闭分部集合 [0] ，关闭后没有剩余分部。
# 总共有 2 种可行的关闭方案。
 

# 提示：
# 1 <= n <= 10
# 1 <= maxDistance <= 10^5
# 0 <= roads.length <= 1000
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= wi <= 1000
# 一开始所有分部之间通过道路互相可以到达。

# Hard
# Floyd最短算法

from math import inf
from typing import List
# @lc code=start
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        # 枚举删除的顶点集合（用二进制掩码表示 0~2^n-1）
        for mask in range(1 << n):
            # Floyd算法，求所有顶点对的最短距离
            # 计dp[u][v]为从顶点u到顶点v的最短距离，初始都为最大
            dp = [[inf] * n for _ in range(n)]
            for u, v, w in roads:
                if mask & (1 << u) == 0 and mask & (1 << v) == 0:
                    dp[u][v] = dp[v][u] = min(dp[u][v], w)

            # 状态转移，依次以k为中间点，更新其他组合的最短距离
            for k in range(n):
                if mask & (1 << k):
                    # k 被删则跳过
                    continue
                for i in range(n):
                    if mask & (1 << i):
                        continue
                    for j in range(i+1, n):
                        if mask & (1 << j):
                            continue
                        dp[i][j] = dp[j][i] = min(dp[i][j], dp[i][k] + dp[k][j])

            # 检查方案可行性
            res += all(dp[u][v] <= maxDistance for u in range(n) for v in range(u+1, n) if mask & (1 << u) == 0 and mask & (1 << v) == 0)

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSets(4, 3, [[2,1,8],[1,0,3],[0,3,8]])) # 6
    print(solution.numberOfSets(3, 5, [[0,1,2],[1,2,10],[0,2,10]])) # 5
    print(solution.numberOfSets(3, 5, [[0,1,20],[0,1,10],[1,2,2],[0,2,2]])) # 7
    print(solution.numberOfSets(1, 10, [])) # 2