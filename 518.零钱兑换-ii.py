#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 假设每一种面额的硬币有无限个。
# 题目数据保证结果符合 32 位带符号整数。

# 示例 1：
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5 = 5
# 5 = 2+2+1
# 5 = 2+1+1+1
# 5 = 1+1+1+1+1

# 示例 2：
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。

# 示例 3：
# 输入：amount = 10, coins = [10]
# 输出：1

# 提示：
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# coins 中的所有值 互不相同
# 0 <= amount <= 5000

from typing import List
# @lc code=start


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 记 dp[j][i]为用前j种硬币，金额i的找零方式数
        # 答案为要求dp[len[coins]-1][amount]
        # 状态转移方程为：
        # dp[j][i] = dp[j-1][i] + dp[j][i - coins[j]] if i > coins[j]
        #          = dp[j-1][i]  if i <= coins[j]
        # dp[j][0] = 1
        # j只依赖j-1，可以降维
        # 又根据dp的形势，迭代i需要正向迭代
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.change(5, [1, 2, 5]))
    print(solution.change(3, [2]))
    print(solution.change(10, [10]))
