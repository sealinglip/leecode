#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
# 由于答案可能会很大，请返回方案数 模 10 ^ 9 + 7 后的结果。

# 示例 1：
# 输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动

# 示例  2：
# 输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动

# 示例 3：
# 输入：steps = 4, arrLen = 2
# 输出：8

# 提示：
# 1 <= steps <= 500
# 1 <= arrLen <= 10 ^ 6

# Hard

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 10 ** 9 + 7
        dp = [0] * (steps + 2)
        dp[0] = 1

        for i in range(steps + 1):
            now = 0
            for j in range(min(i + 1, arrLen)):
                dp[j], now = now, dp[j]
                dp[j] = ((now + dp[j]) % M + dp[j + 1]) % M

        return dp[0]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numWays(3, 2))
    print(solution.numWays(2, 4))
    print(solution.numWays(4, 2))
