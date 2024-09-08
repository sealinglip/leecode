#
# @lc app=leetcode.cn id=3130 lang=python3
#
# [3130] 找出所有稳定的二进制数组 II
#
# 给你 3 个正整数 zero ，one 和 limit 。
# 一个 二进制数组 arr 如果满足以下条件，那么我们称它是 稳定的 ：
# 0 在 arr 中出现次数 恰好 为 zero 。
# 1 在 arr 中出现次数 恰好 为 one 。
# arr 中每个长度超过 limit 的 子数组 都 同时 包含 0 和 1 。
# 请你返回 稳定 二进制数组的 总 数目。

# 由于答案可能很大，将它对 10^9 + 7 取余 后返回。

# 示例 1：
# 输入：zero = 1, one = 1, limit = 2
# 输出：2
# 解释：
# 两个稳定的二进制数组为 [1,0] 和 [0,1] ，两个数组都有一个 0 和一个 1 ，且没有子数组长度大于 2 。

# 示例 2：
# 输入：zero = 1, one = 2, limit = 1
# 输出：1
# 解释：
# 唯一稳定的二进制数组是 [1,0,1] 。
# 二进制数组 [1,1,0] 和 [0,1,1] 都有长度为 2 且元素全都相同的子数组，所以它们不稳定。

# 示例 3：
# 输入：zero = 3, one = 3, limit = 2
# 输出：14
# 解释：
# 所有稳定的二进制数组包括 [0,0,1,0,1,1] ，[0,0,1,1,0,1] ，[0,1,0,0,1,1] ，[0,1,0,1,0,1] ，[0,1,0,1,1,0] ，[0,1,1,0,0,1] ，[0,1,1,0,1,0] ，[1,0,0,1,0,1] ，[1,0,0,1,1,0] ，[1,0,1,0,0,1] ，[1,0,1,0,1,0] ，[1,0,1,1,0,0] ，[1,1,0,0,1,0] 和 [1,1,0,1,0,0] 。


# 提示：
# 1 <= zero, one, limit <= 1000


# @lc code=start
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        # 动态规划
        # 记dp[i][j][k=0 / 1]为i个0、j个1、结尾为k的稳定数组数量
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                if i > limit:
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1] - dp[i - limit - 1][j][1]
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][0] = (dp[i][j][0] % MOD + MOD) % MOD
                if j > limit:
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0] - dp[i][j - limit - 1][0]
                else:
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0]
                dp[i][j][1] = (dp[i][j][1] % MOD + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfStableArrays(1, 1, 2)) # 2
    print(solution.numberOfStableArrays(1, 2, 1)) # 1
    print(solution.numberOfStableArrays(3, 3, 2)) # 14