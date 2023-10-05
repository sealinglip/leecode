#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-30 09:26:00
LastEditors: Thomas Young
LastEditTime: 2020-10-02 08:38:40
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。
# 你也可以先购买，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。

# 示例 1:
# 输入: [7, 1, 5, 3, 6, 4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 总利润为 4 + 3 = 7 。

# 示例 2:
# 输入: [1, 2, 3, 4, 5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

# 示例 3:
# 输入: [7, 6, 4, 3, 1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 提示：
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4

from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 每天的操作之后的状态只有两种情况：0 不持有股票，1 持有股票
        # 设dp(i)[0]为第i天不持有股票的最大收益，dp(i)[1]为第i天持有股票的最大收益
        # dp(i)[0] = max(dp[i-1][1] + prices[i], dp[i-1][0])  0 < i < len(prices)
        # dp(i)[1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  0 < i < len(prices)
        # dp(i) = [0, -prices[0]] if i == 0
        dp = [0, -prices[0]]
        for p in prices[1:]:
            dp = [max(dp[1] + p, dp[0]), max(dp[1], dp[0] - p)]

        return dp[0]

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(solution.maxProfit([1, 2, 3, 4, 5]))  # 4
    print(solution.maxProfit([7, 6, 4, 3, 1]))  # 0
