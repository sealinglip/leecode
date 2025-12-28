# 给你一个整数数组 prices，其中 prices[i] 是第 i 天股票的价格（美元），以及一个整数 k。

# 你最多可以进行 k 笔交易，每笔交易可以是以下任一类型：

# 普通交易：在第 i 天买入，然后在之后的第 j 天卖出，其中 i < j。你的利润是 prices[j] - prices[i]。

# 做空交易：在第 i 天卖出，然后在之后的第 j 天买回，其中 i < j。你的利润是 prices[i] - prices[j]。

# 注意：你必须在开始下一笔交易之前完成当前交易。此外，你不能在已经进行买入或卖出操作的同一天再次进行买入或卖出操作。

# 通过进行 最多 k 笔交易，返回你可以获得的最大总利润。
 

# 示例 1:
# 输入: prices = [1,7,9,8,2], k = 2
# 输出: 14
# 解释:
# 我们可以通过 2 笔交易获得 14 美元的利润：
# 一笔普通交易：第 0 天以 1 美元买入，第 2 天以 9 美元卖出。
# 一笔做空交易：第 3 天以 8 美元卖出，第 4 天以 2 美元买回。

# 示例 2:
# 输入: prices = [12,16,19,19,8,1,19,13,9], k = 3
# 输出: 36
# 解释:
# 我们可以通过 3 笔交易获得 36 美元的利润：
# 一笔普通交易：第 0 天以 12 美元买入，第 2 天以 19 美元卖出。
# 一笔做空交易：第 3 天以 19 美元卖出，第 4 天以 8 美元买回。
# 一笔普通交易：第 5 天以 1 美元买入，第 6 天以 19 美元卖出。
 

# 提示:
# 2 <= prices.length <= 10^3
# 1 <= prices[i] <= 10^9
# 1 <= k <= prices.length / 2

from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # 动规
        # 在每天的状态有：剩余几次交易，当前交易状态：无交易、普通交易、做空交易(用0/1/2表示)
        n = len(prices)
        dp = [[0] * 3 for _ in range(k+1)]

        # 初始化第0天
        for j in range(1, k+1): # j代表完成了几次交易
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i], dp[j][2] - prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j-1][0] + prices[i])

        return dp[k][0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumProfit([1,7,9,8,2], 2)) # 14
    print(solution.maximumProfit([12,16,19,19,8,1,19,13,9], 3)) # 36
