#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#
# 有台奇怪的打印机有以下两个特殊要求：
# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

# 示例 1：
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。

# 示例 2：
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。

# 提示：
# 1 <= s.length <= 100
# s 由小写英文字母组成

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        # 记dp[i][j]为打印区间[i, j]的最小操作数
        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min([dp[i][k] + dp[k + 1][j]
                                    for k in range(i, j)])

        return dp[0][N - 1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.strangePrinter("aaabbb"))
    print(solution.strangePrinter("aba"))
    print(solution.strangePrinter("ababa"))
