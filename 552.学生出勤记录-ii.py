#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。


# 示例 1：
# 输入：n = 2
# 输出：8
# 解释：
# 有 8 种长度为 2 的记录将被视为可奖励：
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。

# 示例 2：
# 输入：n = 1
# 输出：3

# 示例 3：
# 输入：n = 10101
# 输出：183236316


# 提示：
# 1 <= n <= 10^5

# 第一反应的思路：
# n 数的取值范围比较大，所以不能用递归backtrack
# 简化：A只能有一次或零次，问题的结果可以简化为L、P组成n位满足条件2的序列个数+ n * (L、P组成n-1位满足条件2的序列个数)
# 这就很dp了
# 记dp(n)为由L和P组成n位满足条件2的序列个数
# checkRecord(n) = dp(n) + n * dp(n-1)
# dp(n) = 2 * dp(n - 1) - (0 if n < 3 else dp(n - 4))
# 上述思路有问题，有A的串，在去掉A之后不一定是符合条件2的串（比如A恰好在L中间）
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 还是动态规划
        # 记dp(i, j, k)为i天，j次缺勤，末尾连续k次迟到的可奖励次数，0 < i <= n, 0 <= j < 2, 0 <= k < 3
        # 有dp(i, j, 0) = sum(dp(i-1, j, *)) + (sum(dp(i-1, j-1, *)) if j == 1 else 0)
        # dp(i, j, 1) = dp(i-1, j, 0)
        # dp(i, j, 2) = dp(i-1, j, 1)
        # dp(1, 0, 0) = 1, dp(1, 0, 1) = 1, dp(1, 0, 2) = 0, dp(1, 1, 0) = 1, dp(1, 1, 1) = 0, dp(1, 1, 2) = 0
        # 又dp(i, *, *)只依赖dp(i-1, *, *)，所以三维dp可以压缩为二维dp
        dp = [[1, 1, 0], [1, 0, 0]]

        for i in range(2, n + 1):
            # 先算j == 1的情况
            dp[1][0], dp[1][1], dp[1][2] = (sum(
                dp[1]) + sum(dp[0])) % MOD, dp[1][0], dp[1][1]
            # 再算j == 0的情况
            dp[0][0], dp[0][1], dp[0][2] = sum(dp[0]) % MOD, dp[0][0], dp[0][1]

        return (sum(dp[1]) + sum(dp[0])) % MOD


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkRecord(3))  # 19
    print(solution.checkRecord(2))  # 8
    print(solution.checkRecord(1))  # 3
    print(solution.checkRecord(10101))  # 183236316
