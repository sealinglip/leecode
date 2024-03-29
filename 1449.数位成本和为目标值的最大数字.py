#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。

# 如果按照上述要求无法得到任何整数，请你返回 "0" 。


# 示例 1：
# 输入：cost = [4, 3, 2, 5, 6, 7, 2, 5, 5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3 + 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
# 数字     成本
# 1 -> 4
# 2 -> 3
# 3 -> 2
# 4 -> 5
# 5 -> 6
# 6 -> 7
# 7 -> 2
# 8 -> 5
# 9 -> 5

# 示例 2：
# 输入：cost = [7, 6, 5, 5, 5, 6, 8, 7, 8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。

# 示例 3：
# 输入：cost = [2, 4, 6, 2, 4, 6, 4, 4, 4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。

# 示例 4：
# 输入：cost = [6, 10, 15, 40, 40, 40, 40, 40, 40], target = 47
# 输出："32211"


# 提示：
# cost.length == 9
# 1 <= cost[i] <= 5000
# 1 <= target <= 5000

# Hard

from typing import List
# @lc code=start


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 先去重，求dict
        costDict = {}
        for i, c in enumerate(cost):
            costDict[c] = str(i + 1)
        costArr = list(costDict.items())  # （cost, digit)列表
        costArr.sort(key=lambda cd: cd[1])  # 按digit排序

        # 先求最大能有多少位——完全背包问题
        # 背包容量为 target，物品体积为 costArr[i]，价值为 1 的完全背包问题
        # 记dp[i+1][j] 为前i个物品，总体积恰好为j的最大价值和
        # 边界条件：dp[0][j] = 0 if j == 0 else float('-inf')
        # 转移方程：dp[i+1][j] = dp[i][j] if costArr[i] > j
        #                    = max(dp[i][j], 1 + dp[i+1][j-costArr[i]]) if costArr[i] <= j
        # dp[N][target]为所求解
        # 要记录能组成的最大数字，还要记录状态转移的来源，fromDp[i+1][j]
        # fromDp[i+1][j] = j if costArr[i] > j or dp[i][j] > dp[i+1][j-costArr[i]]) >= dp[i][j]
        #              = j - costArr[i] if costArr[i] <= j and (1 + dp[i+1][j-costArr[i]]) >= dp[i][j]

        # 优化：dp 可以降维，去掉i维度
        # fromDp可以省略，回溯时可以根据dp[j] == dp[j-costArr[i]] + 1 来判断从何处转移而来，相等，从j-costArr[i]来，否则从j来
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0

        for c, _ in costArr:
            for j in range(c, target + 1):
                dp[j] = max(dp[j], 1 + dp[j - c])

        if dp[target] < 0:
            return "0"

        res = []
        j = target
        for c, i in costArr[::-1]:
            while j >= c and dp[j] == dp[j - c] + 1:
                res.append(i)
                j -= c

        return "".join(res)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
    print(solution.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12))
    print(solution.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5))
    print(solution.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47))
