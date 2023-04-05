#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#
# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

# 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 - 1 。


# 示例 1：
# 输入：stones = [3, 2, 4, 1], K = 2
# 输出：20
# 解释：
# 从[3, 2, 4, 1] 开始。
# 合并[3, 2]，成本为 5，剩下[5, 4, 1]。
# 合并[4, 1]，成本为 5，剩下[5, 5]。
# 合并[5, 5]，成本为 10，剩下[10]。
# 总成本 20，这是可能的最小值。

# 示例 2：
# 输入：stones = [3, 2, 4, 1], K = 3
# 输出：- 1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。

# 示例 3：
# 输入：stones = [3, 5, 1, 2, 6], K = 3
# 输出：25
# 解释：
# 从[3, 5, 1, 2, 6] 开始。
# 合并[5, 1, 2]，成本为 8，剩下[3, 8, 6]。
# 合并[3, 8, 6]，成本为 17，剩下[17]。
# 总成本 25，这是可能的最小值。


# 提示：
# 1 <= stones.length <= 30
# 2 <= K <= 30
# 1 <= stones[i] <= 100

# Hard
# 复习

from itertools import accumulate
from typing import List
# @lc code=start


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:  # 每合并一次减掉k-1堆，总共要减掉n-1堆，如果不能整除，则无解
            return -1
        # 先求前缀和
        accum = [0] + list(accumulate(stones))
        # 区间dp
        # 记dp[i][j]为合并第i堆到第j堆石头[i,j]为最少堆（即能合并就合并，所以最终堆数一定小于k）的成本
        # dp[i][j] = min(dp[i][p], dp[p+1][j]) + accum[j+1] - accum[i]
        # 初始化dp[i][j] = 0 if j - i < k-1，无解时dp[i][j] = inf
        # 要求dp[0][n-1]
        dp = [[0] * n for _ in range(n)]
        for l in range(k, n+1):
            for i in range(n-l+1):  # 枚举区间七点
                j = i + l - 1
                dp[i][j] = min(dp[i][p] + dp[p+1][j] for p in range(i, j, k-1))
                if (j-i) % (k-1) == 0:  # 可分
                    dp[i][j] += accum[j+1] - accum[i]

        return dp[0][n-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeStones([3, 2, 4, 1], 2))  # 20
    print(solution.mergeStones([3, 2, 4, 1], 3))  # -1
    print(solution.mergeStones([3, 5, 1, 2, 6], 3))  # 25
