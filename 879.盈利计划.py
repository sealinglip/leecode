#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10 ^ 9 + 7 的值。

# 示例 1：
# 输入：n = 5, minProfit = 3, group = [2, 2], profit = [2, 3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。

# 示例 2：
# 输入：n = 10, minProfit = 5, group = [2, 3, 5], profit = [6, 7, 8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0, 1)，(0, 2)，(1, 2)，以及(0, 1, 2) 。

# 提示：
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100

from typing import List
# @lc code=start


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # 变种背包问题
        # 三个维度：当前可选择的工作i，已选择的员工人数j，获利下限k
        # dp(i, j, k) = 前i个工作，选择j人，获利>=k的计划总数
        # 初始条件：dp(0, 0, 0) = 1
        # 状态转移方程为：
        # dp(i, j, k) = dp(i - 1, j, k) if j < group[i]
        # dp(i, j, k) = dp(i - 1, j, k) + dp(i - 1, j - group[i], max(0, k-profit[i]))
        # 题目最终要求 sum([dp(len, i, minProfit) for i in range(0, n + 1)])
        # L = len(group)
        # dp = [[[0] * (minProfit + 1) for _ in range(n + 1)]
        #       for _ in range(L + 1)]
        # dp[0][0][0] = 1
        # for i in range(1, L + 1):
        #     members, earn = group[i - 1], profit[i - 1]
        #     for j in range(n + 1):
        #         for k in range(minProfit + 1):
        #             if j < members:
        #                 dp[i][j][k] = dp[i - 1][j][k]
        #             else:
        #                 dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1]
        #                                [j - members][max(0, k - earn)]) % MOD

        # total = sum(dp[L][j][minProfit] for j in range(n + 1))
        # return total % MOD

        # i 只依赖 i - 1，所以可以降维，遍历j，k时采用逆序
        # dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        # dp[0][0] = 1
        # for g, p in zip(group, profit):
        #     for j in range(n, g - 1, -1):
        #         for k in range(minProfit, -1, -1):
        #             dp[j][k] = (dp[j][k] + dp[j - g][max(0, k - p)]) % MOD

        # total = sum(dp[j][minProfit] for j in range(n + 1))
        # return total % MOD

        # 进一步优化，去掉sum，修改dp的定义
        # 注意：此处dp的定义为dp(j, k) 为当前迭代环节（前i个工作）选择不超过j人，获利>=k的计划总数
        # 所以初始条件为：dp(j, 0) = 1，即在最初迭代环节（前0个工作），最小获利为0的情况，不管员工限制人数为多少（<=j)，总有一种方案（且只有一种，就是谁也不派，实际用工人为0）
        # 重要！！！
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for j in range(n + 1):
            dp[j][0] = 1

        for g, p in zip(group, profit):
            for j in range(n, g - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - g][max(0, k - p)]) % MOD
            # print(dp)

        return dp[n][minProfit]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.profitableSchemes(5, 3, [2, 2], [2, 3]))
    # print(solution.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
