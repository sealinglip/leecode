#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

# 示例 1:
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# 注意:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        # 方法1：动态规划
        # 记dp(i)[0] 为至第i天手上不持股票的最大收益
        #   dp(i)[1] 为至第i天手上持股的最大收益
        # 那么有： dp(i+1)[0] = max(dp(i)[0], dp(i)[1] + prices[i+1])
        #         dp(i+1)[1] = max(dp(i)[1], dp(i)[0] - prices[i+1] - fee)

        dp0 = 0
        dp1 = -prices[0] - fee
        for i in range(1, len(prices)):
            tmp = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i] - fee)
            dp0 = tmp

        return dp0

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))  # 8
    print(solution.maxProfit([1, 3, 7, 5, 10, 3], 3))  # 6
