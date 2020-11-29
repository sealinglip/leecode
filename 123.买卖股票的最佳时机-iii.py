#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-18 08:48:41
LastEditors: Thomas Young
LastEditTime: 2020-10-18 09:20:43
'''
#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:
# 输入: [3, 3, 5, 0, 0, 3, 1, 4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

# 示例 2:
# 输入: [1, 2, 3, 4, 5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

# 示例 3:
# 输入: [7, 6, 4, 3, 1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 每天的操作之后的状态只有五种情况：0 没有交易，持有股票，1 已经发生一次交易，不持有股票，
        # 2 已经发生一次交易，持有股票，3 已经发生两次交易，4 没有交易，不持有股票（这种情况其实不需要考虑）
        # 设dp(i)[j]为第i天第j种情况下的最大交易
        # 
        # dp(i)[0] = max(dp(i-1)[0], -prices[i])  0 < i < len(prices)
        # dp(i)[1] = max(dp(i-1)[1], dp(i)[0] + prices[i])  0 < i < len(prices)
        # dp(i)[2] = max(dp(i-1)[2], dp(i-1)[1] - prices[i])  0 < i < len(prices)
        # dp(i)[3] = max(dp(i-1)[3], dp(i-1)[2] + prices[i])  0 < i < len(prices)
        # dp(i)[4] = 0  0 < i < len(prices) 
        # dp(i) = [-prices[0], -inf, -inf, -inf] i == 0 后三种情况不存在，所以设为负无穷大
        dp = [-float('inf')] * 4
        dp[0] = -prices[0]
        for p in prices[1:]:
            dp = [max(dp[0], -p), max(dp[1], dp[0] + p), max(dp[2], dp[1] - p), max(dp[3], dp[2] + p)]

        return max(*dp, 0) # 0代表第四种情况
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 6, 4, 3, 1]))
    print(solution.maxProfit([1, 2, 3, 4, 5]))
    print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
