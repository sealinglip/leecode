#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2022-11-28 09:51:42
LastEditors: Thomas Young
LastEditTime: 2022-11-28 10:02:12
'''
#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#
# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。

# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

# 返回我们所能得到的最大 分数 是多少。答案误差在 10^-6 内被视为是正确的。


# 示例 1:
# 输入: nums = [9, 1, 2, 3, 9], k = 3
# 输出: 20.00000
# 解释:
# nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
# 我们也可以把 nums 分成[9, 1], [2], [3, 9].
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

# 示例 2:
# 输入: nums = [1, 2, 3, 4, 5, 6, 7], k = 4
# 输出: 20.50000


# 提示:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length


from typing import List
# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 计dp(i, j)为前i+1个元素分成j+1个非空子数组时的最大平均值 i >= j
        # 有dp(i, 0) = sum(nums[:i+1])/(i+1)
        # dp(i, j) = max(dp(l, j-1)+sum(nums[l+1:i+1])/(i-l) for l in range(j-1, i)) i >= j
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        dp[0][0] = nums[0]
        preSum = nums[:]  # 前缀和
        for i in range(1, n):
            preSum[i] += preSum[i-1]

        for i in range(1, n):
            dp[i][0] = preSum[i]/(i+1)
            for j in range(1, min(i+1, k)):
                for l in range(j-1, i):
                    dp[i][j] = max(dp[l][j-1]+(preSum[i]-preSum[l])/(i-l)
                                   for l in range(j-1, i))
        return dp[n-1][k-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestSumOfAverages([9, 1, 2, 3, 9], 3)) # 20
    print(solution.largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4)) # 20.5
