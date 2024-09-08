#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：
# nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
# 以这种方法绘制线条，并返回可以绘制的最大连线数。

# 示例 1：
# 输入：nums1 = [1, 4, 2], nums2 = [1, 2, 4]
# 输出：2
# 解释：可以画出两条不交叉的线，如上图所示。
# 但无法画出第三条不相交的直线，因为从 nums1[1] = 4 到 nums2[2] = 4 的直线将与从 nums1[2] = 2 到 nums2[1] = 2 的直线相交。

# 示例 2：
# 输入：nums1 = [2, 5, 1, 2, 5], nums2 = [10, 5, 2, 1, 5, 2]
# 输出：3

# 示例 3：
# 输入：nums1 = [1, 3, 7, 1, 7, 5], nums2 = [1, 9, 2, 5, 1]
# 输出：2

# 提示：
# 1 <= nums1.length <= 500
# 1 <= nums2.length <= 500
# 1 <= nums1[i], nums2[i] <= 2000

from typing import List
# @lc code=start


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 动态规划
        # 记dp(i, j) 为 nums1[i:] 和 nums2[j:]应用规则能得到的最大连线数
        # 记 M = len(nums1)，M = len(nums2)
        # 有 0 <= i < N，0 <= j < M
        # dp(M - 1, N - 1) = 1 if nums1[M -1] == nums2[N - 1] else 0
        # dp(i, j) = dp(i + 1, j + 1) + 1 if nums1[i] = nums2[j] else max(dp(i + 1, j), dp(i, j + 1))
        # 答案即为dp(0, 0)
        M, N = len(nums1), len(nums2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
    print(solution.maxUncrossedLines(
        [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
    print(solution.maxUncrossedLines(
        [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
