#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


# 示例 1：
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4

# 示例 2：
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9

# 提示：
# 1 <= n <= 10^4

# @lc code=start
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        R = int(sqrt(n))  # 先求根取整
        if R ** 2 == n:
            # 自己就是完全平方数
            return 1
        else:
            # 记dp[i] 为数字i的完全平方数最小拆分数量
            # dp[i] = 1 + min([dp[i - j ** 2] for j in range(sqrt(i) + 1)])
            # dp[0] = 0
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                minV = float('inf')
                for j in range(1, int(sqrt(i))+1):
                    minV = min(minV, dp[i - j ** 2])
                dp[i] = 1 + minV

            return dp[n]


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSquares(12))
    print(solution.numSquares(13))
