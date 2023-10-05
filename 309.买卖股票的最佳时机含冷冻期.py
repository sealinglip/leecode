#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票(即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


# 示例 1:
# 输入: prices = [1, 2, 3, 0, 2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 示例 2:
# 输入: prices = [1]
# 输出: 0

# 提示：
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000


from math import inf
from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 设0,1,2分别对应状态：无股票（非冷冻期）、有股票、冷冻期
        # dp(i, j) 代表前i天后，当前状态为j时的最大利润
        # dp(i, 0) = max(dp(i-1, 2), dp(i-1, 0))
        # dp(i, 1) = max(dp(i-1, 0) - prices[i], dp(i-1, 1))
        # dp(i, 2) = dp(i-1, 1) + prices[i]
        dp = [0, -prices[0], -inf]  # 第0天后不能是冷冻状态，所以设置为-inf

        for p in prices[1:]:
            dp = [max(dp[2], dp[0]), max(dp[0] - p, dp[1]), dp[1] + p]

        return max(dp)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))  # 3
    print(solution.maxProfit([1]))  # 0
