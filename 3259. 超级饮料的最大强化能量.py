# 来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。
# 你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。
# 返回在接下来的 n 小时内你能获得的 最大 总强化能量。
# 注意 你可以选择从饮用任意一种能量饮料开始。

# 示例 1：
# 输入：energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]
# 输出：5
# 解释：
# 要想获得 5 点强化能量，需要选择只饮用能量饮料 A（或者只饮用 B）。

# 示例 2：
# 输入：energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]
# 输出：7
# 解释：
# 第一个小时饮用能量饮料 A。
# 切换到能量饮料 B ，在第二个小时无法获得强化能量。
# 第三个小时饮用能量饮料 B ，并获得强化能量。
 

# 提示：
# n == energyDrinkA.length == energyDrinkB.length
# 3 <= n <= 10^5
# 1 <= energyDrinkA[i], energyDrinkB[i] <= 10^5

from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # 动态规划
        # dp[i][0]代表前i+1个小时，最后一个小时喝A的最大能量
        # dp[i][1]代表前i+1个小时，最后一个小时喝B的最大能量
        # dp[i][0] = max(dp[i-1][0], dp[i-2][1]) + energyDrinkA[i]
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0]) + energyDrinkB[i]
        # 由于dp[i]只依赖dp[i-1]和dp[i-2]，状态可以压缩一下
        dp = [[0] * 2 for _ in range(2)]
        dp[0][0] = energyDrinkA[0]
        dp[0][1] = energyDrinkB[0]
        dp[1][0] = energyDrinkA[0] + energyDrinkA[1]
        dp[1][1] = energyDrinkB[0] + energyDrinkB[1]

        for i in range(2, n):
            # store new dp in dp[0]
            dp[0][0], dp[0][1] = max(dp[1][0], dp[0][1]) + energyDrinkA[i], max(dp[1][1], dp[0][0]) + energyDrinkB[i]
            dp[0], dp[1] = dp[1], dp[0] # swap

        
        return max(dp[1])

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEnergyBoost([1,3,1], [3,1,1])) # 5
    print(solution.maxEnergyBoost([4,1,1], [1,1,3])) # 7
