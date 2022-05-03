#
# @lc app=leetcode.cn id=689 lang=python3
#
# [689] 三个无重叠子数组的最大和
#
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。


# 示例 1：
# 输入：nums = [1, 2, 1, 2, 6, 7, 5, 1], k = 2
# 输出：[0, 3, 5]
# 解释：子数组[1, 2], [2, 6], [7, 5] 对应的起始下标为[0, 3, 5]。
# 也可以取[2, 1], 但是结果[1, 3, 5] 在字典序上更大。

# 示例 2：
# 输入：nums = [1, 2, 1, 2, 1, 2, 1, 2, 1], k = 2
# 输出：[0, 2, 4]


# 提示：
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] < 2^16
# 1 <= k <= floor(nums.length / 3)

# Hard

from typing import List
# @lc code=start


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        prefixSum = [0] * (N + 1)  # make a copy
        # 求前缀和
        for i in range(N):
            prefixSum[i+1] += prefixSum[i] + nums[i]

        # 记dp(i,j)为前i个元素挑选j个长度为k的子数组，能得到的最大和
        # 题目要求的是dp(N, 3)
        # dp(i, j) = max(dp(i-1, j), dp(i-k, j-1) + sum(nums[i-k:i])) if j > 0 and i >= (j * k)
        # 边界条件
        # dp(i, 0) = 0
        # dp(i, j) = 0 if i < (j * k)

        # 因为要输出方案，所以dp需要追溯，取最值时要记录怎么取的最值，所以不能压缩dp存储
        dp = [[0] * 4 for _ in range(N + 1)]
        for j in range(1, 4):
            for i in range(k*j, N+1):
                dp[i][j] = max(dp[i-1][j], dp[i-k][j-1] +
                               prefixSum[i] - prefixSum[i-k])

        res = []
        j = 3
        i = N
        while j > 0:
            while dp[i][j] == dp[i-1][j]:
                i -= 1
            i -= k
            res.append(i)
            j -= 1

        res.reverse()
        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumOfThreeSubarrays(
        [1, 2, 1, 2, 6, 7, 5, 1], 2))  # [0, 3, 5]
    print(solution.maxSumOfThreeSubarrays(
        [1, 2, 1, 2, 1, 2, 1, 2, 1], 2))  # [0, 2, 4]
