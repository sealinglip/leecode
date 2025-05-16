#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#
# 有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
# 给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10 ^ 9 + 7 取模 的值。
# 平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。


# 示例 1:
# 输入: n = 3
# 输出: 5
# 解释: 五种不同的方法如上所示。

# 示例 2:
# 输入: n = 1
# 输出: 1


# 提示：
# 1 <= n <= 1000

# 复习

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * 4 for _ in range(n + 1)] # dp[i] 的四个元素分别代表2 * i的区域，其右 2 * 1区域的四种覆盖情况，分别对应的方法数
        # 0，都没有覆盖；
        # 1：上方被覆盖；
        # 2：上方被覆盖
        # 3：全覆盖——这种铺设才是满足题意的答案，其他三种是为了实现状态转移
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % MOD
        return dp[n][3]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numTilings(1))  # 1
    print(solution.numTilings(3))  # 5
    print(solution.numTilings(4))  # 11
    print(solution.numTilings(5))  # 24
    print(solution.numTilings(1000)) # 979232805
