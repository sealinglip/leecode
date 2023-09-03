#
# @lc app=leetcode.cn id=1388 lang=python3
#
# [1388] 3n 块披萨
#
# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

# 你挑选 任意 一块披萨。
# Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
# Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
# 重复上述过程直到没有披萨剩下。
# 每一块披萨的大小按顺时针方向由循环数组 slices 表示。

# 请你返回你可以获得的披萨大小总和的最大值。


# 示例 1：
# 输入：slices = [1, 2, 3, 4, 5, 6]
# 输出：10
# 解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。

# 示例 2：
# 输入：slices = [8, 9, 8, 6, 1, 1]
# 输出：16
# 解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。


# 提示：
# 1 <= slices.length <= 500
# slices.length % 3 == 0
# 1 <= slices[i] <= 1000

# Hard

from math import inf
from typing import List
# @lc code=start


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calDp(slices: List[int]) -> int:
            N, n = len(slices), (len(slices) + 1) // 3
            dp = [[-inf] * (n+1) for _ in range(N)]
            dp[0][0], dp[0][1] = 0, slices[0]
            dp[1][0], dp[1][1] = 0, max(slices[0], slices[1])
            for i in range(2, N):
                dp[i][0] = 0
                for j in range(1, n + 1):
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + slices[i])
            return dp[N-1][n]

        return max(calDp(slices[1:]), calDp(slices[0:-1]))

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSizeSlices([1, 2, 3, 4, 5, 6]))  # 10
    print(solution.maxSizeSlices([8, 9, 8, 6, 1, 1]))  # 16
