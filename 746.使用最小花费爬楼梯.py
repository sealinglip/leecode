#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-12-21 12:50:46
LastEditors: Thomas Young
LastEditTime: 2020-12-21 12:57:12
'''
#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

# 示例 1:
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

# 示例 2:
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

# 注意：
# cost 的长度将会在[2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为[0, 999]。

from typing import List
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dp = [cost[0], cost[1]]
        N = len(cost)
        if N < 3:
            return dp[N - 1]
        else:
            for i in range(2, N):
                tmp = min(dp[0], dp[1]) + cost[i]
                dp[0], dp[1] = dp[1], tmp
        return min(dp)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
