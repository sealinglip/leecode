#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1：
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

# 示例 2：
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

# 提示：
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

# Hard
from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = {}
        # 记dp(i, j, s)为第i天剩余j次交易机会时的最大收益，0 <= i < len(prices), 0 <= j <= k, s 为0 或 1 分别代表当前手里没有股票和有股票
        # dp(i, j, 0) = max(dp(i - 1, j, 0), dp(i - 1, j, 1) + prices[i])
        # dp(i, j, 1) = max(dp(i - 1, j, 1), dp(i - 1, j + 1, 0) - prices[i])

        dp[k] = [0, None]
        for price in prices:
            for j in range(k):
                if (j + 1) in dp:
                    tmp = [None, None]
                    if j in dp:
                        tmp[0] = max(
                            dp[j][0], dp[j][1] + price) if dp[j][0] is not None else dp[j][1] + price
                        tmp[1] = max(dp[j][1], dp[j + 1][0] - price)
                    elif dp[j + 1][0] is not None:
                        tmp[1] = dp[j + 1][0] - price
                    else:
                        continue
                    dp[j] = tmp

        maxDp = 0
        for j in dp:
            tmp = dp[j]
            if tmp[0]:
                maxDp = max(maxDp, tmp[0])
            if tmp[1]:
                maxDp = max(maxDp, tmp[1])

        return maxDp
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(2, [2, 4, 1]))  # 2
    print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # 7
