#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-10 14:06:45
@LastEditors: Thomas Young
@LastEditTime: 2020-07-10 15:19:10
'''
#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票(即冷冻期为 1 天)。

# 示例:
# 输入: [1, 2, 3, 0, 2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        days = len(prices)
        dp = [0 for i in range(days + 2)]  # dp[i]代表从本日起的最大利润

        for i in range(days-2, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i + 1, days):
                if prices[i] < prices[j]:
                    dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2])

        return dp[0]

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
    print(solution.maxProfit([1, 2, 4]))
